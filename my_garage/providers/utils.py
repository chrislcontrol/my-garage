from decimal import Decimal


def convert_string_price_to_decimal(string: str) -> Decimal:
    return Decimal(string.replace('.', "").replace(",", ".").replace("R$", "").strip())
