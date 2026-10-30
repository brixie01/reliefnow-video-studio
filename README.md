# ReliefNow Video Studio

**ReliefNow Laser Centers' own AI video editor, on a Mac or Windows PC.** Every edit comes out in the ReliefNow brand by default: green `#8BBE29` on charcoal, Open Sans, and the ReliefNow logo top-left. The brand lives in `tools/brandkit.py`, `tools/style.json` and `assets/logo.png`; every video gets the ReliefNow badge top-left (ReliefNow Centers + "Ditch the Drugs and Skip the Scalpel"). Ask Claude for "just the ReliefNow logo", "just the tagline" or "no logo" and it sets `"logo_style"` (`logo` / `tagline` / `none`) for that video. Drop in a talking-head or screen-demo video. Claude cuts the retakes, repeats and dead air, writes the captions, places motion graphics that never cover your face, and adds sound effects. You pick the look in a step-by-step Studio and **see every choice play on your own video before you render.**

No CapCut, no timeline, no stock footage. Your videos never leave your computer.

> Based on [Video Edit Studio](https://github.com/Deym0121/video-edit-studio) by Joshua Ladero (MIT license, kept in `LICENSE`).

---

## What you get

| | |
|---|---|
| **Studio wizard** | Start → Colours → Fonts → Hook → Captions → Visuals → Extras → Watch, in English or Taglish. Every card plays on *your* video, with the real sound effects. |
| **Live preview** | The motion graphics are real HTML scenes, so the phone preview plays them instantly in your colours and fonts. No render needed. |
| **🗣 Tell Claude what you want** | A design brief: tap the platform, vibe, captions and graphics, then say the look in your own words (Taglish is fine). The Studio builds the look from it and shows why each part changed, and Auto-edit and your notes follow it. |
| **🎬 Learn a style from videos you like** | Add up to 3 videos from creators you like. The Studio studies their captions, colours, pacing and graphics (never their footage), and you mix them part by part into your own style or a Brand Kit. |
| **✨ Auto-edit with Claude** | One button runs the whole editorial pass, following your brief (needs [Claude Code](https://docs.claude.com/en/docs/claude-code/overview)). |
| **🎯 Hook Lab** | Finds your strongest 2–7 s lines, proposes a thumbnail title, and copies the best one to the top as a cold open. |
| **🩺 Edit Health** | Flags words said twice, clipped words, dead air, "filtered" HDR colour, graphics over your face, text under the TikTok/Reels buttons, a missing hook and quiet audio. Each item has a one-click fix or a jump-to button. |
| **💬 Talk to edit** | Pause where something's wrong, type or say "tanggalin 'to", and Claude applies every note. |
| **📦 Post Kit** | 9:16 + 1:1 + 16:9 videos, captions (.srt), a cover image and the post caption, in one zip. |
| **🎨 Brand Kits** | Save your look and use it on every video, or share it as a file. |
| **2026 motion library** | 44 trending motion graphics: marker annotations, target rings, a magnifier loupe, before/after wipes, 3D device frames, phone alerts, search bars, feed scrolls, social post cards, tier lists, scorecards, price slashes, countdowns, charts, word clouds, split-flap boards, glitch titles, redacted reveals, myth/fact flips, polaroids and confetti. Also 19 hook styles and 8 caption styles. |
| **Natural colour** | iPhone HDR is converted to normal colour (Apple's own tone mapping on a Mac), so the edit looks like your camera. |

## Install

📘 Step-by-step guides: **[English](docs/GUIDE.md)** · **[Taglish](docs/GABAY.md)** · 📺 4-min screen-share tutorial (`docs/tutorial/Studio_Tutorial.mp4`)

**From GitHub (gets updates):**

1. Install [Git for Windows](https://git-scm.com/download/win) and the [Claude app](https://claude.ai/download), and sign in with your own Claude account. Accept the invitation to the private `brixie01/reliefnow-video-studio` repository (GitHub emails it).
2. In the Claude app's **Code** tab, choose your Documents folder and say:

> clone https://github.com/brixie01/reliefnow-video-studio and install it

Sign in to GitHub when the window pops up. Claude downloads it, runs the installer (about 30 minutes, ≈ 8 GB) and starts the Studio at **http://localhost:8765**. Later, say **"update the Studio"** in that folder to get the newest version (`git pull`).

**From a zip:**

1. Unzip `reliefnow-video-studio.zip` (right-click → **Extract All**) and put the `reliefnow-video-studio` folder somewhere easy, such as your Documents folder.
2. Install the [Claude app](https://claude.ai/download), sign in with your own Claude account, go to the **Code** tab and choose that folder.
3. Say:

> install this

Claude runs the installer (about 30 minutes, ≈ 8 GB downloaded), checks everything and starts the Studio at **http://localhost:8765**. Click **Allow** when it asks to run a command. After that, start it any time by saying "start the Studio" in that folder, or with `.\vedit.cmd studio` (Windows) / `./vedit studio` (Mac).

Your copy is yours alone: your projects, videos and renders stay on your computer and are separate from everyone else's.

**By hand, on a Mac** (Terminal):

```bash
./tools/setup.sh          # ≈ 8 GB with the models · --lite for a smaller install
./vedit doctor            # checks every piece
./vedit studio            # opens http://localhost:8765
```

**By hand, on Windows** (PowerShell, in the folder):

```powershell
powershell -ExecutionPolicy Bypass -File tools\setup.ps1     # -Lite for a smaller install
.\vedit.cmd doctor
.\vedit.cmd studio
```

**Requirements:**
- **Mac:** macOS on Apple Silicon, plus the Xcode Command Line Tools (`xcode-select --install`)
- **Windows:** Windows 10 or 11, 64-bit. No Python or admin rights needed. For "install this" in the Claude app, also [Git for Windows](https://git-scm.com/download/win)
- about 10 GB of free space

Everything installs inside this folder: no system packages and no password.

## Use it

1. **Start** → upload a video. It is transcribed and cleaned automatically, and iPhone HDR becomes natural colour.
2. Pick your **colours, fonts, hook, captions, graphics and extras**. Hover a card to watch it; click to pick it and hear it on your video.
3. **Watch** → *Render preview*. Run **Edit Health**, leave notes, then *Export final 1080p* and build the **Post Kit**.

Prefer chatting? Open the folder in Claude Code and say *"i-edit mo 'tong video na 'to"*. The same pipeline runs (`.claude/skills/reliefnow-video-edit/SKILL.md`).

## How it works

```
upload ─► tosdr (natural colour) ─► vedit transcribe (Whisper) ─► vedit plan (cuts at energy dips)
       ─► Claude: decisions.json (cuts, hook, keywords) + scenes.json (motion graphics)
       ─► mograph (HTML/GSAP → alpha video) ─► sfx ─► vedit render (captions, graphics, sound) ─► health checks
```

| File | What it does |
|---|---|
| `tools/vedit.py` | Transcribe, plan, render and verify |
| `tools/mograph.py` + `tools/mograph_more.py` | Motion-graphic templates |
| `tools/sfx.py` | Synthesized sound design |
| `tools/health.py` | Edit Health |
| `tools/editor/` | The Studio: `studio.html`, `studio_pro.js`, `studio_api.py`, `studio_pro.py`, `server.py` |
| `DESIGN_SYSTEM.md` | Brand and motion rules |
| `reference/motion_trends_2026.md` | Research behind the 2026 library |

## License

MIT: see `LICENSE`. The bundled fonts are SIL OFL 1.1, and the installer downloads models and tools under their own licenses (one of them, the MMS model, is non-commercial). Details are in `THIRD_PARTY_NOTICES.md`.

## Privacy

The Studio runs on `127.0.0.1` only. Your videos, transcripts and renders stay in `input/`, `work/` and `output/`, and `.gitignore` keeps them out of git. Auto-edit sends your transcript to Claude through your own Claude Code account; nothing else leaves your computer.

**There is no sign-in.** Anyone who can reach the Studio can watch, change and remove every video, so it only ever listens on this computer or a private Tailscale network. It still protects itself: it answers only to its own address (other websites open in your browser can't control it), no web address can reach files outside its folders, every change is written to `logs/activity.log` with the address it came from, and **Remove / Replace move a project to `trash/` for 30 days** (move its folders back to undo) before it is deleted for good.

## Share it with a couple of people (Tailscale)

The Studio stays on one computer (this one), which does all the work; the others open it in their browser over Tailscale, a free private network only the people you invite can join. Don't put it on Netlify/Vercel (they can't run it) or the open internet (there is no sign-in).

1. Install Tailscale on this computer and sign in (https://tailscale.com/download). Invite the other people; each installs Tailscale on their own computer and signs in.
2. In the Tailscale app on this computer, note its **IP** (`100.x.y.z`) and its **name** (e.g. `reliefnow-pc`, or `reliefnow-pc.tailXXXX.ts.net`).
3. Create or edit `studio.json` in this folder (next to `README.md`):
   ```json
   { "name": "ReliefNow Studio", "listen": "100.x.y.z", "allowed_hosts": ["reliefnow-pc", "reliefnow-pc.tailXXXX.ts.net", "100.x.y.z"] }
   ```
   Never set `"listen"` to `0.0.0.0`: that opens it to the whole office or café network.
4. Restart the Studio (`.\vedit.cmd studio`). Everyone opens `http://reliefnow-pc:8765`. On this computer, too, use that address (`localhost` no longer answers while it listens on Tailscale).
Alternatively, keep `"listen": "127.0.0.1"` and run `tailscale serve --bg 8765` for an HTTPS link (`https://<name>.<tailnet>.ts.net`); put that name in `"allowed_hosts"`.

**Start it automatically (Windows):** a scheduled task can run `tools\start-studio.cmd` hidden whenever you sign in, so the Studio is always on at http://localhost:8765 (output: `logs\studio.log`). Double-clicking `tools\start-studio.cmd` starts it by hand.

5. Keep this computer on and awake while people use it. Two people working on the same video at the same time overwrite each other's changes: one video, one person.

## Limits (today)

- On Windows, transcription runs on the CPU (faster-whisper), so it's slower than on Apple Silicon, and the person cut-out, face finder and text finder use open-source models (DeepLabV3, OpenCV, RapidOCR) instead of Apple Vision. `.github/workflows/windows.yml` installs and runs the whole path on a clean Windows machine (start it by hand under Actions).
- Linux isn't tested yet.
- The live preview plays graphics exactly. Two pieces, the text behind you and the shrink card, show the last render, because they need the person cut-out.
- It is a single-user local app, not a hosted service.
