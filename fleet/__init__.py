"""Multi-Agent Fleet for OpenAkari-Codex.

Tier1/Tier2 architecture aligned with ADR 0042-v2:
  Tier1 — Single Opus Supervisor (existing cron)
  Tier2 — Up to 32 Fast Model Fleet Workers (scheduler-dispatched)

Quick start:
    python3 -m fleet.console              # interactive control panel
    python3 -m fleet.console -w 4         # start 4 workers immediately
    python3 -m fleet.scheduler            # headless scheduler (no interactive input)
"""
