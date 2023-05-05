# Test prefix phone tree
import unittest

from models import Pricing
from prefix_phone_tree import PrefixPhoneTree
from models import Pricing


class TestPrefixPhoneTree(unittest.TestCase):

    def test_init_tree(self):
        """
        Test when init tree then expect a tree is initialized
        """
        tree = PrefixPhoneTree()
        self.assertIsNotNone(tree)
        self.assertEqual(tree._root, {})

    def test_insert_new_prefix_when_prefix_was_not_existed(self):
        """
        Test when insert new prefix to tree then expect prefix in inserted in the tree
        """
        pricing = Pricing(
            prefix="46",
            operator_id="operator_A",
            price=1.1
        )
        tree = PrefixPhoneTree()
        tree.insert(pricing)
        self.assertIsNotNone(tree._root.get('4'))
        self.assertIsNotNone(tree._root['4'].get('6'))
        self.assertIsNotNone(tree._root['4']['6'].get('#'))
        self.assertEqual(tree._root['4']['6']['#'], pricing)

    def test_insert_new_prefix_when_prefix_was_existed_but_lower_price(self):
        """
        Test when insert new prefix to tree, the prefix was existed but lower price then replace price with lower value
        for existed prefix
        """
        prefix = "46"
        old_pricing = Pricing(
            prefix=prefix,
            operator_id="operator_A",
            price=1.1
        )
        new_pricing = Pricing(
            prefix=prefix,
            operator_id="operator_B",
            price=1.0
        )
        tree = PrefixPhoneTree()
        tree.insert(old_pricing)
        tree.insert(new_pricing)
        self.assertEqual(tree._root['4']['6']['#'], new_pricing)

    def test_insert_new_prefix_when_prefix_was_existed_but_higher_price(self):
        """
        Test when insert new prefix to tree, the prefix was existed but higher price then do nothing
        """
        prefix = "46"
        old_pricing = Pricing(
            prefix=prefix,
            operator_id="operator_A",
            price=1.1
        )
        new_pricing = Pricing(
            prefix=prefix,
            operator_id="operator_B",
            price=1.2
        )
        tree = PrefixPhoneTree()
        tree.insert(old_pricing)
        tree.insert(new_pricing)
        self.assertEqual(tree._root['4']['6']['#'], old_pricing)

    def test_find_the_cheapest_operator_for_phone_number_when_only_1_matched_prefix(self):
        """
        Test find the cheapest operator when only 1 matched prefix then return the pricing
        """
        pricing = Pricing(
            prefix="46",
            operator_id="operator_A",
            price=1.1
        )
        tree = PrefixPhoneTree()
        tree.insert(pricing)
        result = tree.find_the_cheapest_operator("4680912312")
        self.assertIsNotNone(result)
        self.assertEqual(result, pricing)

    def test_find_the_cheapest_operator_for_phone_number_when_2_matched_prefix(self):
        """
        Test find the cheapest operator when 2 matched prefix then return the pricing of the longest matched prefix
        """
        pricing_1 = Pricing(
            prefix="46",
            operator_id="operator_A",
            price=1.1
        )
        pricing_2 = Pricing(
            prefix="468",
            operator_id="operator_A",
            price=1.5
        )
        tree = PrefixPhoneTree()
        tree.insert(pricing_1)
        tree.insert(pricing_2)
        result = tree.find_the_cheapest_operator("4680912312")
        self.assertIsNotNone(result)
        self.assertEqual(result, pricing_2)

    def test_find_the_cheapest_operator_for_phone_number_no_prefix_match(self):
        """
        Test find the cheapest operator when no prefix matches then return None
        """
        pricing = Pricing(
            prefix="46",
            operator_id="operator_A",
            price=1.1
        )
        tree = PrefixPhoneTree()
        tree.insert(pricing)
        result = tree.find_the_cheapest_operator("458097732")
        self.assertIsNone(result)

    def test_find_the_cheapest_operator_for_phone_number_with_prefix_matched_two_operators(self):
        """
        Test find the cheapest operator when no prefix matches then return None
        """
        pricing_1 = Pricing(
            prefix="46732",
            operator_id="operator_A",
            price=1.1
        )
        pricing_2 = Pricing(
            prefix="467",
            operator_id="operator_B",
            price=1.0
        )
        tree = PrefixPhoneTree()
        tree.insert(pricing_1)
        tree.insert(pricing_2)
        result = tree.find_the_cheapest_operator("46732000000")
        self.assertIsNotNone(result)
        self.assertEqual(result, pricing_2)