from subprocess import run

paths = [
    'projects/multi-agent-review-survey/logs/2026-03-26T02:16:43+08:00-fleet-沙弥香-01-1774462571-e3c01b-main-report-closeout.md',
    'projects/multi-agent-review-survey/git_commit_shamika_1774462571.py',
    'projects/multi-agent-review-survey/git_commit_shamika_1774462571_log.py',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/沙弥香-01-1774462571-e3c01b] add session log for main report closeout'], check=True)
