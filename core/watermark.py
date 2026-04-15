"""Watermark utilities (skeleton).

This module will apply protective watermark overlays for preview images.
"""

from pathlib import Path


def apply_watermark(input_image: Path, output_image: Path, mode: str = "tiled") -> Path:
    """Apply a watermark placeholder operation and return output path.

    Args:
        input_image: Source image path.
        output_image: Destination path for watermarked image.
        mode: Watermark mode, for example "center" or "tiled".

    Returns:
        Path to the produced watermarked image.
    """
    _ = (input_image, mode)
    return output_image
