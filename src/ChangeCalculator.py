class ChangeCalculator:
    # Fixed EUR to BGN exchange rate according to ECB
    EUR_TO_BGN_EXCHANGE_RATE = 1.95583

    @staticmethod
    def get_total(currency: str) -> float:
        """
        The user should insert the value of their bill
        """
        total = float(input(f"Total {currency}: "))
        return total

    @staticmethod
    def get_payment_amount(currency: str) -> float:
        """
        The user should enter the payment amount
        """
        payment_amount = float(input(f"You pay with (in {currency}): "))
        return payment_amount

    @staticmethod
    def convert_bgn_to_eur(value: float) -> float:
        """
        The function converts the provided amount of money from BGN to EUR
        Example: 10 leva -> 5.11 euro
        """
        return value / ChangeCalculator.EUR_TO_BGN_EXCHANGE_RATE

    @staticmethod
    def convert_eur_to_bgn(value: float) -> float:
        """
        The function converts the provided amount of money from EUR to BGN
        Example: 10 euro -> 19.56 leva
        """
        return value * ChangeCalculator.EUR_TO_BGN_EXCHANGE_RATE