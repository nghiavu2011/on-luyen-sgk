---
name: command-batching
description: >-
  Use when executing multiple shell commands, file edits, or tool calls.
  Minimizes user approval prompts by batching operations into fewer tool calls.
metadata:
  aas-category: discipline
  aas-risk: low
  aas-source: custom
  aas-date-added: '2026-10-02'
  triggers: run_command, shell, terminal, multiple commands, batch, script, reduce prompts
---

# Command Batching — Minimize Approval Prompts

## Iron Law

**Every tool call costs the user one approval click. Fewer calls = faster workflow.**

## Why This Exists

Antigravity's UI requires user approval for every `run_command`, `write_to_file`, and `replace_file_content` call. When an agent makes 10 separate calls, the user must click "Allow" + "Submit" **10 times**. This skill reduces that to 1–3 clicks.

## The Rules

### Rule 1: Chain Shell Commands

**NEVER** call `run_command` multiple times when commands can be chained.

```
❌ BAD (3 approval prompts):
  run_command: mkdir -p src/components
  run_command: mkdir -p src/utils
  run_command: npm init -y

✅ GOOD (1 approval prompt):
  run_command: mkdir -p src/components src/utils && npm init -y
```

**Chaining operators:**
- `&&` — run next only if previous succeeds (preferred)
- `;` — run next regardless
- `|` — pipe output

### Rule 2: Script for 4+ Commands

When you need **4 or more** sequential commands, write a **single script file** then execute it in one call.

```
❌ BAD (6 approval prompts):
  run_command: npm install express
  run_command: npm install cors
  run_command: npm install dotenv
  run_command: mkdir -p src/routes
  run_command: mkdir -p src/middleware
  run_command: npm run build

✅ GOOD (2 approval prompts — 1 write + 1 run):
  write_to_file: setup.ps1
    npm install express cors dotenv
    New-Item -ItemType Directory -Force -Path src/routes, src/middleware
    npm run build

  run_command: powershell -ExecutionPolicy Bypass -File setup.ps1
```

**Script location:** Use the `scratch/` directory in the artifact folder for temporary scripts.

### Rule 3: Batch File Edits

**NEVER** make multiple `replace_file_content` calls for the same file in the same logical change when a single `write_to_file` with `Overwrite: true` is cleaner.

```
❌ BAD (3 approval prompts for 1 file):
  replace_file_content: config.ts (edit 1)
  replace_file_content: config.ts (edit 2)
  replace_file_content: config.ts (edit 3)

✅ GOOD (1 approval prompt):
  write_to_file: config.ts (Overwrite: true) — full new content
```

**Exception:** For large files where only 1-2 small edits are needed, a single `replace_file_content` is fine. The rule targets *multiple* edits to the *same* file.

### Rule 4: Parallel Independent Calls

When tool calls are **independent of each other**, make them all in the **same function_calls block**.

```
❌ BAD (sequential, 3 rounds of approval):
  Round 1: write_to_file: src/a.ts
  Round 2: write_to_file: src/b.ts
  Round 3: write_to_file: src/c.ts

✅ GOOD (parallel, 1 round of approval):
  Round 1:
    write_to_file: src/a.ts
    write_to_file: src/b.ts
    write_to_file: src/c.ts
```

### Rule 5: Combine Install Commands

**NEVER** install packages one by one.

```
❌ BAD:
  run_command: npm install react
  run_command: npm install react-dom
  run_command: npm install next

✅ GOOD:
  run_command: npm install react react-dom next
```

This applies to all package managers: `npm`, `pip`, `cargo`, `go get`, etc.

### Rule 6: Pre-check Before Multi-step

Before executing a multi-step operation, **gather all info in one command** instead of multiple.

```
❌ BAD (3 prompts):
  run_command: node --version
  run_command: npm --version
  run_command: git --version

✅ GOOD (1 prompt):
  run_command: node --version && npm --version && git --version
```

## Quick Reference — Batching Cheatsheet

| Scenario | Strategy | Max Prompts |
|----------|----------|-------------|
| 2-3 shell commands | Chain with `&&` | 1 |
| 4+ shell commands | Write script → run script | 2 |
| Multiple edits, same file | `write_to_file` with Overwrite | 1 |
| Multiple edits, different files | Parallel tool calls | 1 |
| Multiple package installs | Single install command | 1 |
| Info gathering | Chain with `&&` | 1 |

## Red Flags — STOP and Batch

If you are about to:
- Call `run_command` **3+ times in a row** → STOP. Chain or script.
- Call `replace_file_content` on the **same file 3+ times** → STOP. Use Overwrite.
- Install packages **one at a time** → STOP. Combine.
- Make **sequential independent** tool calls → STOP. Parallelize.

## Valid Exceptions

- Commands that **depend on previous output** (need to read result before next step)
- **Interactive commands** that require `send_input`
- **Long-running daemons** that must be started separately
- Commands on **different working directories** that can't be chained

## Limitations
- This skill optimizes agent behavior only. It cannot disable the platform's approval UI.
- Use this skill only when the task clearly matches the scope described above.
