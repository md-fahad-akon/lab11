from typing import Dict, Optional

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Implementation of the 'initial' operator."""

    def operate(self, text: str, params: Optional[Dict] = None) -> str:
        # Remove leading/trailing spaces and split into words
        words = text.strip().split()

        # Take the first character of each word, uppercase it, and add a dot
        initials = [f"{word[0].upper()}." for word in words if word]

        # Join with a space, e.g. ["J.", "S."] -> "J. S."
        return " ".join(initials)

    def operator_name(self) -> str:
        return "initial"

    def validate(self, params: Optional[Dict] = None) -> None:
        # No special params yet
        return None

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
