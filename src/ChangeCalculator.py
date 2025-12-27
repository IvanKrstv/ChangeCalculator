class ChangeCalculator:
    # Fixed EUR to BGN exchange rate according to the ECB
    EUR_TO_BGN_EXCHANGE_RATE = 1.95583

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