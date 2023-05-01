from typing import Optional

from models import Pricing


class PrefixPhoneTree:

    def __init__(self):
        self._root = {}

    def insert(self, new_pricing: Pricing):
        """
        insert new pricing.
        If prefix hasn't existed, insert new one
        If prefix was existed, compare price to the new one. If new pricing has lower price the replacing old one.
        """
        current = self._root
        for ch in new_pricing.prefix:
            # if character doesn't exist in children then create a new one
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        if "#" in current:
            # prefix was inserted before with a pricing. Compare its price with the new one's price
            old_pricing: Pricing = current["#"]
            if new_pricing.price < old_pricing.price:
                current["#"] = new_pricing
        else:
            # add pricing for prefix
            current["#"] = new_pricing

    def find_the_cheapest_operator(self, phone_number: str) -> Optional[Pricing]:
        """
        Find the cheapest operator for phone number.
        If no operator contains prefix for phone number. Return None
        Complexity of this method is O(n) with n is the length of phone number
        :param phone_number: user's phone number
        :return: the cheapest operator or none.
        """
        result: Optional[Pricing] = None
        current = self._root
        for ch in phone_number:
            if ch not in current:
                # stop searching
                return result
            # get the pricing of the longest prefix. If prefix doesn't have prefix, result is None
            result = current[ch].get("#")
            current = current[ch]
        return result
