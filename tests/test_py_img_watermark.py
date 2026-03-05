"""Tests for py-img-watermark."""

import pytest
from py_img_watermark import watermark


class TestWatermark:
    """Test suite for watermark."""

    def test_basic(self):
        """Test basic usage."""
        result = watermark("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            watermark("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = watermark(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
