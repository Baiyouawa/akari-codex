import subprocess

files = [
    'projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md',
    'projects/multi-agent-survey-review/README.md',
    'projects/multi-agent-survey-review/TASKS.md',
    'projects/multi-agent-survey-review/logs/2026-03-26T23:48:38+08:00-fleet-智乃-02-1774539789-a7a30d-fix-locked-sample-detailed-notes.md',
    'projects/multi-agent-survey-review/plans/修复十篇综述统一样本集详读笔记-确保与最终筛选结果和下载-manifest-完全一致.md',
    'projects/multi-agent-survey-review/plans/修复十篇综述统一样本集详读笔记-确保与最终筛选结果和下载-manifest-完全一致-progress.md',
    'projects/multi-agent-survey-review/plans/修复十篇综述统一样本集详读笔记-确保与最终筛选结果和下载-manifest-完全一致-self-review.md',
    'projects/multi-agent-survey-review/plans/修复十篇综述统一样本集详读笔记-确保与最终筛选结果和下载-manifest-完全一致-summary.md',
]

subprocess.run(['git', 'add', *files], check=True)
subprocess.run(['git', 'commit', '-m', '[fleet/智乃-02-1774539789-a7a30d] fix locked-sample detailed reading notes'], check=True)
