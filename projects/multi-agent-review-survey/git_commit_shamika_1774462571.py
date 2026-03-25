from subprocess import run

paths = [
    'projects/multi-agent-review-survey/README.md',
    'projects/multi-agent-review-survey/TASKS.md',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/沙弥香-01-1774462571-e3c01b] close out main report task'], check=True)
