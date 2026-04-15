"""Project storage utilities (skeleton).

This module will manage project folder structure, JSON persistence,
and ZIP export of previews/finals.
"""

from pathlib import Path


def create_project_structure(project_id: str, base_dir: Path = Path("projects")) -> Path:
    """Create a placeholder project directory and return its path.

    Args:
        project_id: Unique project identifier.
        base_dir: Base directory where projects are stored.

    Returns:
        Path to the project root directory.
    """
    project_path = base_dir / project_id
    project_path.mkdir(parents=True, exist_ok=True)
    return project_path


def save_json(data: dict, destination: Path) -> None:
    """Placeholder JSON save function.

    Args:
        data: Dictionary to persist.
        destination: Output JSON file path.
    """
    _ = (data, destination)
