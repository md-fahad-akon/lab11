import re
from typing import Dict, Optional

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Implementation of the 'initial' operator."""

    def operate(self, text: str, params: Optional[Dict] = None) -> str:
        match = re.search(r"[A-Za-z0-9]", text)
        if not match:
            return text

        first_index = match.start()

        raw_prefix = text[:first_index]
        prefix_chars = [ch for ch in raw_prefix if not ch.isspace()]
        prefix = "".join(prefix_chars)

        tail = text[first_index:]

        words = tail.strip().split()

        initials = [f"{word[0].upper()}." for word in words if word]

        initials_text = " ".join(initials)

        return prefix + initials_text

    def operator_name(self) -> str:
        return "initial"

    def validate(self, params: Optional[Dict] = None) -> None:
        return None

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
