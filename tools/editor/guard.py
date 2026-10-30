"""Request checks and the activity log, used by server.py (the Studio has no sign-in: access is whoever can reach it,
so keep it on this computer or a private Tailscale network).

  Host       only this Studio's own names (blocks DNS rebinding); studio.json "allowed_hosts" adds e.g. the Tailscale name
  Origin     a browser sends Origin on every POST: it must be this same Studio, so other websites can't drive it
  Path       no backslashes, drive letters or parent folders in a URL, so no route can reach files outside its folder
  Activity   logs/activity.log: one JSON line per upload, change, render and removal, with the address it came from
"""
from __future__ import annotations

import json
import socket
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "logs" / "activity.log"
_lock = threading.Lock()


def allowed_hosts(extra=()):
    return {"localhost", "127.0.0.1", "[::1]", socket.gethostname().lower()} | {x.lower() for x in extra}


def host_ok(host_header, extra=()):
    host = (host_header or "").strip().lower()
    host = host.split("]")[0] + "]" if host.startswith("[") else host.split(":")[0]
    return host in allowed_hosts(extra)


def origin_ok(origin, host_header):
    """Same host and port as the request itself. No Origin = not from a web page (CLI, scripts): allowed."""
    if not origin:
        return True
    o = urlparse(origin)
    return bool(o.netloc) and o.netloc.lower() == (host_header or "").strip().lower()


def path_ok(path):
    """Decoded URL path."""
    return not ("\\" in path or ":" in path or "\x00" in path or any(seg in ("..", ".") for seg in path.split("/")))


def log(ip, action, **detail):
    LOG.parent.mkdir(exist_ok=True)
    line = json.dumps(dict(t=time.strftime("%Y-%m-%d %H:%M:%S"), ip=ip, action=action, **detail), ensure_ascii=False)
    with _lock, open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
