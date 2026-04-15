"""Image preparation utilities (skeleton).

This module will contain helpers for resizing, cropping, and basic
normalization of product images before rendering.
"""

from pathlib import Path


def prepare_product_images(input_paths: list[Path], output_dir: Path) -> list[Path]:
    """Prepare product images for downstream rendering.

    Args:
        input_paths: Paths to source product images.
        output_dir: Directory where processed images should be saved.

    Returns:
        A list of paths to processed images.
    """
    _ = (input_paths, output_dir)
    return []
