"""Module: password_validator.py
Utility for validating password strength.
"""

import re
from typing import Pattern

# Pre‑compiled regular expression that enforces:
#   • Minimum 8 characters
#   • At least one lowercase letter
#   • At least one uppercase letter
#   • At least one digit
_PASSWORD_PATTERN: Pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')


def is_valid_password(password: str) -> bool:
    """Validate a password against the defined strength policy.

    The password is considered valid when it satisfies **all** of the
    following criteria:

    * Minimum length of 8 characters.
    * Contains at least one uppercase letter.
    * Contains at least one lowercase letter.
    * Contains at least one digit.

    Parameters
    ----------
    password: str
        The password string to validate.

    Returns
    -------
    bool
        ``True`` if the password meets the policy, otherwise ``False``.
    """
    if not isinstance(password, str):
        return False
    return bool(_PASSWORD_PATTERN.match(password))