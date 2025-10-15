import re

EMAIL_RE = re.compile(r'^[A-Za-z0-9._%+-]+@university\.com$')
PASS_RE  = re.compile(r'^[A-Z][A-Za-z]{5,}\d{3,}$')

def is_valid_email(s: str) -> bool:
    return bool(EMAIL_RE.fullmatch(s or ""))

def is_valid_password(s: str) -> bool:
    return bool(PASS_RE.fullmatch(s or ""))

import re

EMAIL_RE = re.compile(r'^[A-Za-z0-9._%+-]+@university\.com$')
PASS_RE  = re.compile(r'^[A-Z][A-Za-z]{5,}\d{3,}$')

def is_valid_email(s: str) -> bool:
    return bool(EMAIL_RE.fullmatch(s or ""))

def is_valid_password(s: str) -> bool:
    return bool(PASS_RE.fullmatch(s or ""))
