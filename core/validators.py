"""Input validation helpers (skeleton).

This module will validate required fields and basic constraints for
uploaded files and product brief content.
"""


def validate_brief(brief: dict) -> tuple[bool, list[str]]:
    """Validate minimal product brief fields.

    Args:
        brief: User-provided product brief dictionary.

    Returns:
        Tuple of (is_valid, list_of_errors).
    """
    _ = brief
    return True, []


def validate_image_count(count: int, min_count: int, max_count: int) -> tuple[bool, str]:
    """Validate that an image count is within expected bounds.

    Args:
        count: Actual uploaded image count.
        min_count: Minimum allowed count.
        max_count: Maximum allowed count.

    Returns:
        Tuple of (is_valid, message).
    """
    if min_count <= count <= max_count:
        return True, "OK"
    return False, f"Количество изображений должно быть от {min_count} до {max_count}."
