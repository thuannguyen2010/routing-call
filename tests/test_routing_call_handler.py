import unittest

from models import OperatorPrice, Operator
from routing_call_handler import RoutingCallHandler


class TestInitRoutingCallHandler(unittest.TestCase):
    def test_init_routing_call_handler(self):
        """
        Test init routing call handler with 2 operators when init handler successfully
        """
        operator_a = Operator(
            id='A',
            price_lists=[
                OperatorPrice(prefix="1", price=0.9),
            ]
        )
        operator_b = Operator(
            id='B',
            price_lists=[
                OperatorPrice(prefix="1", price=0.92),
                OperatorPrice(prefix="467", price=1.0),
                OperatorPrice(prefix="48", price=1.2),
            ]
        )
        operators = [operator_a, operator_b]
        handler = RoutingCallHandler(operators)
        self.assertIsNotNone(handler)


class TestRoutingCallHandler(unittest.TestCase):

    def setUp(self) -> None:
        operator_a = Operator(
            id='A',
            price_lists=[
                OperatorPrice(prefix="1", price=0.9),
                OperatorPrice(prefix="4673", price=0.9),
                OperatorPrice(prefix="46732", price=1.1),
            ]
        )
        operator_b = Operator(
            id='B',
            price_lists=[
                OperatorPrice(prefix="1", price=0.92),
                OperatorPrice(prefix="467", price=1.0),
                OperatorPrice(prefix="48", price=1.2),
            ]
        )
        operators = [operator_a, operator_b]
        self.handler = RoutingCallHandler(operators)

    def test_find_the_cheapest_price_for_phone_number(self):
        """
        Test find the cheapest operator when only 1 matched prefix then return the pricing
        """
        result = self.handler.routing_call("48042213123")
        self.assertIsNotNone(result)
        self.assertEqual(result.price, 1.2)

    def test_find_the_cheapest_operator_for_phone_number_when_2_matched_prefix(self):
        """
        Test find the cheapest operator when 2 matched prefix then return the pricing of the longest matched prefix
        """
        result = self.handler.routing_call("467323214214")
        self.assertIsNotNone(result)
        self.assertEqual(result.price, 1.1)

    def test_find_the_cheapest_operator_for_phone_number_no_prefix_match(self):
        """
        Test find the cheapest operator when no prefix matches then return None
        """
        result = self.handler.routing_call("2343433353535")
        self.assertIsNone(result)

    def test_find_the_cheapest_operator_for_not_normalized_phone_number(self):
        """
        Test find the cheapest operator when phone number if not normalized
        """
        result = self.handler.routing_call("+48-0422-13123")
        self.assertIsNotNone(result)
        self.assertEqual(result.price, 1.2)
