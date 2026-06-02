from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_limit_price
)

from bot.logging_config import logger


def main():

    try:

        symbol = input(
            "Enter Symbol (e.g. BTCUSDT): "
        ).upper()

        side = input(
            "Enter Side (BUY/SELL): "
        ).upper()

        order_type = input(
            "Enter Order Type (MARKET/LIMIT): "
        ).upper()

        quantity = float(
            input("Enter Quantity: ")
        )

        price = None

        if order_type == "LIMIT":
            price = float(
                input("Enter Price: ")
            )

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_limit_price(
            order_type,
            price
        )

        print("\nORDER REQUEST")
        print("-" * 30)
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price is not None:
            print(f"Price: {price}")

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )
        else:
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nORDER RESPONSE")
        print("-" * 30)
        print(
            f"Order ID: "
            f"{response.get('orderId')}"
        )
        print(
            f"Status: "
            f"{response.get('status')}"
        )
        print(
            f"Executed Qty: "
            f"{response.get('executedQty')}"
        )

        if response.get("avgPrice"):
            print(
                f"Average Price: "
                f"{response.get('avgPrice')}"
            )

        print("\nOrder Successful!")

    except ValueError as e:
        print(f"\nValidation Error: {e}")

    except Exception as e:
        logger.exception(
            "Application Error"
        )
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
    validate_symbol(symbol)