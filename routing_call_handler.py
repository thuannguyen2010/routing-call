from typing import List

from models import Operator
from prefix_phone_tree import PrefixPhoneTree


class RoutingCallHandler:
    def __init__(self, operators: List[Operator]):
        """
        init the trie for prefix phone number. With two prefixes are the same, we take the cheaper one
        the complexity of init tree function is O(mxnxl), with:
        m = number of operators
        n = length of price lists in each operator
        l = average length of prefixes
        :param operators: operator inputs
        """
        self._prefix_phone_trie = PrefixPhoneTree()
        for operator in operators:
            for pricing in operator.get_pricing_lists():
                self._prefix_phone_trie.insert(pricing)

    def _normalize_phone_number(self, phone_number) -> str:
        result = ""
        for c in phone_number:
            if c.isdigit():
                result += c
        return result

    def routing_call(self, phone_numer: str):
        normalized_phone_number = self._normalize_phone_number(phone_numer)
        return self._prefix_phone_trie.find_the_cheapest_operator(normalized_phone_number)
