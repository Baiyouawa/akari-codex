from subprocess import run

paths = [
    'projects/multi-agent-review-survey/README.md',
    'projects/multi-agent-review-survey/TASKS.md',
    'projects/multi-agent-review-survey/logs/2026-03-26T01:42:08+08:00-fleet-灯里-08-1774460467-e28c8e-candidate-survey-verification-closeout.md',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/灯里-08-1774460467-e28c8e] close survey-verification task'], check=True)
