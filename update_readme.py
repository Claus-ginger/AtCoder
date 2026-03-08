from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re


def count_python_files(directory: Path) -> int:
    """指定ディレクトリ以下の .py ファイル数を数える"""
    if not directory.exists():
        return 0
    return sum(1 for file in directory.rglob("*.py") if file.is_file())


def main() -> None:
    repo_root = Path(".")
    readme_path = repo_root / "README.md"

    targets = [
        repo_root / "tessoku",
        repo_root / "ABC",
    ]

    solved_problems = sum(count_python_files(target) for target in targets)
    today = datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()

    new_stats_block = (
        "<!-- START_SECTION:stats -->\n"
        f"- Solved problems: {solved_problems}\n"
        f"- Last updated: {today}\n"
        "<!-- END_SECTION:stats -->"
    )

    readme_text = readme_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"<!-- START_SECTION:stats -->.*?<!-- END_SECTION:stats -->",
        re.DOTALL,
    )

    updated_text = pattern.sub(new_stats_block, readme_text)
    readme_path.write_text(updated_text, encoding="utf-8")


if __name__ == "__main__":
    main()
