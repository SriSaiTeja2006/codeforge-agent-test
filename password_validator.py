"""password_validator.py
Utility for validating passwords according to the project's security policy.

The original implementation exposed a simple ``add`` helper.  The core
functionality is provided by :func:`is_valid_password`.  For backward
compatibility the historic name :func:`validate_password` is retained as a
thin wrapper around the new implementation.
"""

from __future__ import annotations

from typing import Any

def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*.

    This function is kept for compatibility with earlier versions of the
    module that exposed a trivial arithmetic helper.
    """
    return a + b


def is_valid_password(password: Any) -> bool:
    """Return ``True`` if *password* satisfies the project's password policy.

    Validation rules:

    1. The input must be a string. Non‑string values are rejected.
    2. After stripping leading and trailing whitespace the password must
       contain at least one non‑whitespace character.
    3. The stripped password must be **at least 8 characters long**.

    Empty strings (``""``) and strings consisting solely of whitespace
    (e.g. ``"   "``) are rejected.  Leading or trailing whitespace does not
    contribute to the length check, ensuring that a password that appears
    non‑empty only because of surrounding spaces is not mistakenly accepted.

    Parameters
    ----------
    password: Any
        The value to validate.  Typically a ``str``; any non‑string input
        results in ``False``.

    Returns
    -------
    bool
        ``True`` if the password meets all criteria, otherwise ``False``.
    """
    if not isinstance(password, str):
        return False

    # Remove surrounding whitespace – this prevents a password that is only
    # spaces from being considered valid and ensures the length check is based
    # on the actual characters the user entered.
    stripped = password.strip()

    # Reject empty or whitespace‑only passwords.
    if not stripped:
        return False

    # Enforce the minimum length requirement.
    return len(stripped) >= 8


# --------------------------------------------------------------------------- #
# Backward‑compatibility shim
# --------------------------------------------------------------------------- #
def validate_password(password: Any) -> bool:
    """Compatibility wrapper for the original public API.

    Historically the module exported ``validate_password``.  Internally the
    implementation now lives in :func:`is_valid_password`.  This wrapper simply
    forwards the call, preserving the original name for existing code and the
    test suite.
    """
    return is_valid_password(password)


__all__ = [
    "add",
    "is_valid_password",
    "validate_password",
]