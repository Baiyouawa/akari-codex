#!/usr/bin/env python3
"""批量导入表情包到小白收藏夹。

用法：
    # 导入一个文件夹里的所有图片
    python3 scripts/import_stickers.py /path/to/sticker/folder

    # 导入单张图片
    python3 scripts/import_stickers.py /path/to/image.jpg

    # 导入后自动用 Vision LLM 打标签（需要 API 可用）
    python3 scripts/import_stickers.py /path/to/folder --auto-tag

    # 从 QQ 表情包收藏目录直接导入（NapCat 缓存目录）
    python3 scripts/import_stickers.py /path/to/napcat/image_cache
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}


def main() -> None:
    parser = argparse.ArgumentParser(description="批量导入表情包到小白收藏夹")
    parser.add_argument("path", help="图片文件或文件夹路径")
    parser.add_argument("--auto-tag", action="store_true", help="导入后自动用 Vision LLM 打标签")
    parser.add_argument("--tags", nargs="*", default=[], help="给所有导入的图片加上这些标签")
    parser.add_argument("--source", default="manual-import", help="来源标记")
    args = parser.parse_args()

    from runner.sticker_manager import save_sticker_from_file, auto_tag_sticker

    target = Path(args.path)
    if not target.exists():
        print(f"路径不存在: {args.path}")
        sys.exit(1)

    if target.is_file():
        files = [target]
    else:
        files = sorted(
            f for f in target.rglob("*")
            if f.is_file() and f.suffix.lower() in IMAGE_EXTS
        )

    if not files:
        print(f"没有找到图片文件 (支持: {', '.join(IMAGE_EXTS)})")
        sys.exit(1)

    print(f"找到 {len(files)} 张图片，开始导入...")

    imported = 0
    skipped = 0
    for i, f in enumerate(files, 1):
        entry = save_sticker_from_file(
            f,
            tags=list(args.tags),
            source_user=args.source,
        )
        if entry:
            imported += 1
            print(f"  [{i}/{len(files)}] 导入: {f.name} → {entry['id']}")
            if args.auto_tag:
                try:
                    tags = auto_tag_sticker(entry["id"])
                    if tags:
                        print(f"         标签: {', '.join(tags)}")
                except Exception as e:
                    print(f"         自动标签失败: {e}")
        else:
            skipped += 1
            print(f"  [{i}/{len(files)}] 跳过（重复或太小）: {f.name}")

    print(f"\n完成！导入 {imported} 张，跳过 {skipped} 张")
    print(f"收藏目录: {_project_root / 'logs' / 'xiaobai' / 'stickers'}")


if __name__ == "__main__":
    main()
