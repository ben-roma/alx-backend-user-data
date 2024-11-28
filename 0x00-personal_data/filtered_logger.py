#!/usr/bin/env python3
"""Module for obfuscating log messages"""

import re
from typing import List

def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Obfuscate the message by replacing field values with redaction"""
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1={}{}'.format(redaction, separator), message)
