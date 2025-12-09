from typing import Dict, Optional

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Minimal implementation of the 'initial' operator for Task 3."""

    def operate(self, text: str, params: Optional[Dict] = None) -> str:
        # For now, Task 3 doesn't care what operate does.
        # We'll improve this in later tasks.
        return text

    def operator_name(self) -> str:
        # This is exactly what your test is asserting.
        return "initial"

    def validate(self, params: Optional[Dict] = None) -> None:
        # No special params to validate yet.
        return None

    def operator_type(self) -> OperatorType:
        # This is an anonymization operator.
        return OperatorType.Anonymize
