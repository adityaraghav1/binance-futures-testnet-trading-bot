VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]
def validate_side(side):
    if side.upper() not in VALID_SIDES:
        raise ValueError(
            "Side must be BUY or SELL"
        )
def validate_order_type(order_type):
    if order_type.upper() not in VALID_TYPES:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )
def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than 0"
        )
def validate_limit_price(order_type, price):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError(
                "LIMIT order requires a price"
            )
def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError(
            "Symbol should be like BTCUSDT"
        )
