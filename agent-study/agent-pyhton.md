# Agent Guide — Pyhton

Read `../AGENTS.md` first. It holds the repo-wide rules. This file covers only the **Pyhton** course.

## Location

```
Pyhton/index.html                     course catalogue
Pyhton/README.md                      human-facing course documentation
Pyhton/catatan/*.html                 chapter notes
Pyhton/catatan/bab * mentahan.md      raw source material, not published
Pyhton/praktikum/praktikum_3*.py      lab exercises
Pyhton/soal/soal_praktikum_3*.md      practice questions
```

This course is the odd one out. It uses `catatan/`, not `modul/`, and it mixes HTML notes with Python scripts and Markdown exercises. There is no `modul/gambar/` folder.

Note the directory name is misspelled `Pyhton` in the repo. Keep it. Do not rename it, that would break every existing link.

Files named `bab * mentahan.md` are raw material the author pastes in before a chapter is written. They are incomplete on purpose, contain formatting debris, and are never published. Read them to learn what the author wants covered, then write the real HTML. Do not link to them from any page.

## Current inventory

| Chapter | File | Sections | Tables | Code blocks |
| --- | --- | --- | --- | --- |
| 01 Get started | `catatan/bab 1 - Get started.html` | 29 | 1 | 27 |
| 02 Python Dasar | `catatan/bab 2 - Python Dasar.html` | 44 | 2 | 65 |
| 03 Input, Output, dan Interaksi | `catatan/bab 3 - Input Output dan Interaksi dengan Pengguna.html` | 10 | 3 | 47 |
| 04 Operator Perbandingan, Boolean, Percabangan | `catatan/bab 4 - Operator Perbandingan Boolean dan Percabangan.html` | 34 | 7 | 119 |

The catalogue plans eight chapters. Five through eight are still unwritten:

- 05 Loop dan Perulangan (`while`, `for`, `range()`)
- 06 Function (parameter, nilai balik, cakupan variabel)
- 07 List, Tuple, Dictionary, dan Set
- 08 File, Exception, Module, dan OOP

Scripts: `praktikum/praktikum_32.py` through `praktikum/praktikum_37.py`.

Exercises: `soal/soal_praktikum_32.md` through `soal/soal_praktikum_37.md`, one Markdown file per script, numbered to match. Files 32 to 35 carry no `## Soal` heading, while 36 and 37 carry eight and nine. Match the newer style for anything added.

## Feature gap — this course is behind

All four chapters have the sticky topbar, the light and dark theme, and the version note box. **None has an interactive quiz or the mobile slide-in table of contents.**

Missing:

- mobile slide-in table of contents (`#menu`, `#scrim`, `.toc`)
- `KUIS_DATA` quiz with feedback, explanation, next button, score, and `localStorage` progress

The quiz engine already exists at `D:\opencode\quiz.js` and the drawer at `D:\opencode\nav.js`. Both were extracted from the Fisika modules, which are at full parity. **Port those, do not rewrite them.**

## Chapter template

Chapters 03 and 04 follow this shape. Follow it for the remaining chapters.

- fixed-width side table of contents in `<nav class="toc">`, shown only above 1280px
- `.wrap` containing `.topbar`, then `header.hero`
- the quote block directly after the hero, see the animation rule below
- `.box` version note naming Python 3.14.x
- roughly 30 to 35 `<h2>` sections, TOC lists only the `h2` ids
- `.box` recap of the rules, then `<footer>` with the sources actually used

Reuse the whole `<style>` block from chapter 04 unchanged. It already carries `.box`, `.tight`, and `.quote-highlight`.

## Content rules specific to this subject

### Runnable code

Every code block shown to the reader must actually run. Before committing, execute each snippet. A tutorial that prints something different from what the surrounding prose claims is worse than no tutorial.

Also match the output written in the prose to the real output. This bit chapter 04: the code printed `Boleh mengakses fitur dewasa` while the page claimed `Boleh akses fitur dewasa`. Run the program, then write down what it really prints.

### Python is case sensitive

`list` and `List` are different names, and so are `True`, `False`, and `None`. Spell them exactly as Python requires. This is the single most common defect in student-facing Python material.

### No language mixing in identifiers

Use `snake_case` for variables and functions, `PascalCase` for classes, `UPPER_SNAKE` for constants. Do not write Indonesian variable names, and do not abbreviate. `total_price`, not `harga` and not `tot`.

### Exercise and script must match

When you add `praktikum_38.py`, add `soal/soal_praktikum_38.md` in the same change. The numbering is shared between the script and its exercise file. A script without an exercise is incomplete work here.

### Explain the error message

Errors are teaching material. When a snippet can fail, show the actual traceback and explain the line that caused it. Do not present code that only works when everything goes right.

The exception is the literal traceback text, which is English and trips `check.py`. Paraphrase the meaning in Indonesian and name the error class in prose, then test the snippet to confirm the class is right. Chapter 03 and 04 both do this.

### Version note

State the Python version these notes target. Behaviour differs across versions, particularly around string formatting and error messages. Chapters 03 and 04 use the `.box` callout for this and say Python 3.14.x.

### The quote block

Each chapter opens with the line "Banyak cara untuk menuju satu tujuan" inside `.quote-highlight`. It sits directly after `header.hero` and animates in once on page load: `quote-masuk` fades and lifts it, then `quote-sorot` sweeps a highlight across the text. Keep both keyframes and the `prefers-reduced-motion` fallback.

## Validation

```bash
cd /d/APK/DeVault/Learning
git status --short

cd /d/opencode
python check.py "py4c*.html"    # adjust the glob to the chunks you actually wrote
```

Confirm `FILES CHECKED` equals the number of chunk files you created. The validator does not check Python at all.

Then run every script:

```bash
cd /d/APK/DeVault/Learning/Pyhton/praktikum
python praktikum_38.py
```

And execute every code block from the finished chapter. Write a throwaway harness that extracts each `<pre><code>`, pipes a scripted stdin at the ones that call `input()`, and compare stdout with the output block that follows. Blocks meant to fail must be listed separately or they read as breakage.

## Two traps that cost real time

**A green validator is not proof.** `check.py` misses glued words inside a single token. Chapter 04 shipped `decisionsehari-hari`, `Begins dari`, `Bagian ini.opsional`, and `Moreau generally` with `TOTAL PROBLEMS: 0`. Always read the generated text yourself, sentence by sentence.

**Python keywords are not English words.** `not`, `is`, `while`, `else`, and `none` are language tokens, but `check.py` originally flagged them as English prose, so any chapter using `not` failed validation. The keyword list and common variable names are now in the `ALLOW` tuple at the top of `check.py`. If a future word trips the validator and is plainly a code token, add it there rather than rewriting the code.

## Git

Commit message style, in Indonesian, describing what was added. Stage only files under `Pyhton/`. Never commit `D:\opencode`. Never commit unless the user asks.

The author reorganises folders on their own without asking first. Expect the tree to shift between sessions, and re-read the tree before relying on any path recorded here.