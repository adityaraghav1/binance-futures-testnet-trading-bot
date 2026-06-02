from bot.client import client
from bot.logging_config import logger
def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET ORDER REQUEST: "
            f"{symbol} {side} {quantity}"
        )
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(
            f"MARKET RESPONSE: {response}"
        )
        return response
    except Exception:
        logger.exception(
            "Market order failed"
        )
        raise
def place_limit_order(
    symbol,
    side,
    quantity,
    price
):
    try:
        logger.info(
            f"LIMIT ORDER REQUEST: "
            f"{symbol} {side} "
            f"{quantity} {price}"
        )
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(
            f"LIMIT RESPONSE: {response}"
        )
        return response
    except Exception:
        logger.exception(
            "Limit order failed"
        )
        raise
