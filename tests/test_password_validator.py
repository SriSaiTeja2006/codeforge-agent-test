"""Unit tests for the password_validator module using pytest."""

import sys
from pathlib import Path

import pytest

# Ensure the repository root is in sys.path so that the module can be imported
repo_root = Path(__file__).resolve().parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Import the function under test
try:
    from password_validator import is_valid_password
except ImportError:  # pragma: no cover
    # Fallback for when the test file is executed as part of a package
    from .password_validator import is_valid_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Hello123", True),          # valid password
        ("", False),                 # empty password
        ("Ab1", False),              # too short
        ("hello123", False),         # missing uppercase
        ("HELLO123", False),         # missing lowercase
        ("HelloWorld", False),       # missing digit
    ],
)
def test_is_valid_password(password: str, expected: bool) -> None:
    """Validate that `is_valid_password` returns the expected result."""
    assert is_valid_password(password) is expected