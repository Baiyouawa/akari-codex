from subprocess import run

paths = [
    'projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md',
    'projects/multi-agent-review-survey/TASKS.md',
    'projects/multi-agent-review-survey/README.md',
    'projects/multi-agent-review-survey/logs/2026-03-26T02:19:21+08:00-fleet-柑奈-02-1774462721-f2ece3-final-10-idea-field-alignment.md',
]

run(['git', 'add', *paths], check=True)
run(['git', 'commit', '-m', '[fleet/柑奈-02-1774462721-f2ece3] align final 10-idea fields'], check=True)
