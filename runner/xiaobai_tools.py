"""小白工具兼容层 — 已迁移至 runner.tools 统一工具层。

所有联网工具（web_search / web_fetch / get_current_time / calculate）
现在由 ToolExecutor 统一管理，不再通过 function calling 调用。

此文件保留仅为向后兼容，新代码请使用 runner.tools.ToolExecutor。
"""

from .tools import ToolExecutor as _TE  # noqa: F401
