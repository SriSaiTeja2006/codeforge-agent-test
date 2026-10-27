"""Unit tests for password_validator module using pytest."""
import sys
from pathlib import Path
import pytest

# Ensure root workspace directory is in sys.path
repo_root = Path(__file__).resolve().parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

try:
    from password_validator import add
except ImportError:
    from .password_validator import add

def test_add_positive():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-5, 5) == 0

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -5) == -5
