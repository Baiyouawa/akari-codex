from subprocess import run

paths = [
    'projects/multi-agent-review-survey/README.md',
    'projects/multi-agent-review-survey/TASKS.md',
    'projects/multi-agent-review-survey/logs/2026-03-26T02:55:18+08:00-fleet-灯里-08-1774464884-da7688-download-final-confirmed-pdfs-closeout.md',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/灯里-08-1774464884-da7688] close out final confirmed pdf download task'], check=True)
