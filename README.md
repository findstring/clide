<h1 align="center">CLIDE</h1>
<p align="center"><b>C L</b>anguage <b>I</b>ntegrated <b>D</b>evelopment <b>E</b>nvironment</p>
<p align="center">A tiny, no-frills C code editor built with Python + tkinter.</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.0.1-orange">
  <img src="https://img.shields.io/badge/python-3.x-blue">
  <img src="https://img.shields.io/badge/platform-Windows-lightgrey">
</p>

> 🤖 **Note:** This README was written by Claude AI, because the dev (me) was too lazy to write one myself. The code, however, is 100% hand-written — except for the giant list of C keywords/types/functions used for syntax highlighting, which Claude also helped generate because who's memorizing `stdc_leading_zeros` for fun.

---

## What is this?

CLIDE is a lightweight C editor with syntax highlighting, line numbers, auto-indent, and a one-key "compile and run" workflow using `gcc`. No bloat, no plugins, no 400 MB Electron shell — just a `tkinter` window that gets out of your way.

Built mostly as a personal project / learning exercise, not (yet) a serious rival to VS Code.

## Features

- 🎨 **Syntax highlighting** for C — keywords, types, functions, strings, char literals, comments (single-line and block), numbers, and preprocessor directives
- 🔢 **Line numbers** that track scrolling and zoom
- 🔍 **Zoom in/out** with `Ctrl + Mouse Wheel`
- ⏎ **Auto-indent** — adds/removes indentation automatically after `{`, `}`, and `:`
- ▶️ **Run with F5** — compiles your file with `gcc` and runs it in a new console window
- 💾 **Open / Save / Save As** from the File menu or `Ctrl+O` / `Ctrl+S`
- 📋 **Paste-aware highlighting** — pasted multi-line code gets highlighted properly, not just the current line
- 🖱️ Undo/redo support (unlimited undo history)

## Requirements

- Python 3.x with `tkinter` (usually bundled with Python on Windows)
- `gcc` installed and available on your system `PATH` (for the Run feature)
- Windows — the "Run" feature and maximized window launch currently rely on Windows-specific behavior (see Limitations below)

## Getting Started

```bash
git clone https://github.com/findstring/clide
cd clide
python clide.py
```

Open a `.c` file with `Ctrl+O`, write some code, hit `F5` to compile and run it.

## Version

**v0.0.1** — early days. Things work, but expect rough edges.

## Limitations

- **Windows-only for now.** The maximized-window launch and the `F5` run command (`cmd /k gcc ...`) both assume Windows. Running this on Linux/macOS will likely misbehave or crash on the run step.
- **Single-line-focused highlighting.** Typing re-highlights the line you're on; large structural edits elsewhere in the file (outside of paste) aren't automatically re-scanned.
- **No project/workspace support** — it's a single-file editor, not a full IDE. No multi-file tabs yet.
- **No build configuration** — compilation is a hardcoded `gcc file.c -o file.exe`, no custom flags, no Makefile support.
- **No autocomplete, linting, or error highlighting** — you find out about bugs when `gcc` yells at you.
- **No find & replace** yet.
- **Font dependency** — defaults to the `Iosevka` font; falls back to `Courier New` if it's not installed on your system.

## To Be Featured (Roadmap)

- [ ] Cross-platform support (Linux/macOS build + run)
- [ ] Find & Replace
- [ ] Multiple tabs / multi-file projects
- [ ] Custom compiler flags / build settings
- [ ] Bracket matching + auto-close brackets
- [ ] Inline error markers from `gcc` output
- [ ] Themes (because everyone deserves a light mode option, even if nobody will use it)
- [ ] Proper packaging (so you don't need Python installed to run it)

## Contributing

This is a small personal project, but if you spot a bug or have an idea, feel free to open an issue or PR.

## License

See [LICENSE](LICENSE) for details.
