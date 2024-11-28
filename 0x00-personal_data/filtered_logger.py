#!/usr/bin/env python3
"""
This module defines a function `filter_datum` that obfuscates log messages.
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message obfuscated.

    Args:
        fields (list): A list of strings representing all fields to obfuscate.
        redaction (str): A string representing by what the field will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is separating
                         all fields in the log line (message).

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}', f'{field}={redaction}{separator}', message)
    return message
