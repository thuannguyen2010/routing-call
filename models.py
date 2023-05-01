from dataclasses import dataclass
from typing import List


@dataclass
class Pricing:
    prefix: str
    price: float
    operator_id: str


@dataclass
class OperatorPrice:
    prefix: str
    price: float


@dataclass
class Operator:
    id: str
    price_lists: List[OperatorPrice]

    def get_pricing_lists(self) -> List[Pricing]:
        pricing_lists: List[Pricing] = []
        for price in self.price_lists:
            pricing_lists.append(
                Pricing(
                    prefix=price.prefix,
                    price=price.price,
                    operator_id=self.id
                )
            )
        return pricing_lists
