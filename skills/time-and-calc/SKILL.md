---
name: time-and-calc
description: "Use when you need the current time/date or need to compute a mathematical expression"
complexity: low
model-minimum: glm-5
disable-model-invocation: false
allowed-tools: ["get_current_time", "calculate"]
---

# /time-and-calc

Utility skill for time queries and mathematical calculations.

## get_current_time

Returns the current date and time in Beijing timezone (UTC+8), including day of week.

**When to use**: User asks "现在几点", "今天星期几", scheduling/reminder context needs current time.

## calculate

Safely evaluates mathematical expressions using Python's `math` module.

**Supported**: All `math` functions (`sqrt`, `sin`, `cos`, `log`, `exp`, `pi`, `e`, ...) plus `abs`, `round`, `min`, `max`, and standard operators (`+`, `-`, `*`, `/`, `**`, `%`).

**When to use**: User asks for computation, unit conversion, statistical formulas, etc.

**Examples**:
- `sqrt(144)` → 12.0
- `2**10` → 1024
- `log(1000, 10)` → 3.0
- `pi * 3.5**2` → 38.48...

## Constraints

- `calculate` runs in a sandboxed eval — no file I/O, no imports, no side effects
- Only numeric/math operations; string manipulation not supported
