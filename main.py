# Routing calls system
from models import Operator, OperatorPrice
from routing_call_handler import RoutingCallHandler

if __name__ == '__main__':
    operator_a = Operator(
        id='A',
        price_lists=[
            OperatorPrice(prefix="1", price=0.9),
            OperatorPrice(prefix="268", price=5.1),
            OperatorPrice(prefix="46", price=0.17),
            OperatorPrice(prefix="4620", price=0.0),
            OperatorPrice(prefix="468", price=0.15),
            OperatorPrice(prefix="4631", price=0.15),
            OperatorPrice(prefix="4673", price=0.9),
            OperatorPrice(prefix="46732", price=1.1),
        ]
    )
    operator_b = Operator(
        id='B',
        price_lists=[
            OperatorPrice(prefix="1", price=0.92),
            OperatorPrice(prefix="44", price=0.5),
            OperatorPrice(prefix="46", price=0.2),
            OperatorPrice(prefix="467", price=1.0),
            OperatorPrice(prefix="48", price=1.2),
        ]
    )
    operators = [operator_a, operator_b]
    handler = RoutingCallHandler(operators)
    input_phone_numbers = ["+46-73-212345", "68123456789", "+4481737232"]
    for phone_number in input_phone_numbers:
        result = handler.routing_call(phone_number)
        if result:
            print(
                f"the cheapest operator for phone number {phone_number} is {result.price} "
                f"with operator_id={result.operator_id}, prefix={result.prefix}")
        else:
            print(f"no available operator for phone number {phone_number}")

