from subprocess import run

paths = [
    'projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md',
    'projects/multi-agent-review-survey/TASKS.md',
    'projects/multi-agent-review-survey/README.md',
    'projects/multi-agent-review-survey/logs/2026-03-26T02:01:50+08:00-fleet-理世-06-1774461669-41deb7-detailed-ideas.md',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/理世-06-1774461669-41deb7] add 10 detailed survey ideas'], check=True)
