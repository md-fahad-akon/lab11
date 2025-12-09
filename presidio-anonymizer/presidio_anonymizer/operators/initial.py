from typing import Dict, Optional

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    def operate(self, text: str, params: Optional[Dict] = None) -> str:
        return text

    def operator_name(self) -> str:
        return "initial"

    def validate(self, params: Optional[Dict] = None) -> None:
        return None

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
