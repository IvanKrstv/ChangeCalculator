import flet as ft
from ChangeCalculator import ChangeCalculator


CURRENCIES = ("BGN", "EUR")
DEFAULT_CURRENCY = CURRENCIES[0] # BGN
CONVERSION = {
    'EUR': ChangeCalculator.convert_bgn_to_eur,
    'BGN': ChangeCalculator.convert_eur_to_bgn
}


def main(page: ft.Page):
    # Logic
    def update_currency(e, amount: ft.TextField, currency: str) -> None:
        if currency == amount.data:
            return

        money = float(amount.value) if amount.value else 0.0
        converted_money = CONVERSION[currency](money)

        amount.value = f"{converted_money:.2f}"
        amount.data = currency

        page.update()


    def update_change(e) -> None:
        total = float(total_input.value) if total_input.value else 0.0
        payment_amount = float(payment_amount_input.value) if payment_amount_input.value else 0.0

        result = payment_amount - total
        change_output.value = f"{result:.2f}"
        page.update()



    def create_bgn_button(textfield: ft.TextField) -> ft.Button:
        return ft.Button(
            content="BGN",
            on_click=lambda e: update_currency(e, amount=textfield, currency="BGN")
        )

    def create_eur_button(textfield: ft.TextField) -> ft.Button:
        return ft.Button(
            content="EUR",
            bgcolor=ft.Colors.BLUE_100,
            on_click=lambda e: update_currency(e, amount=textfield, currency="EUR")
        )

    # Row with BGN EUR buttons for the user to choose from
    def currency_row(textfield: ft.TextField) -> ft.Row:
        return ft.Row(
            controls=[
                create_bgn_button(textfield),
                create_eur_button(textfield)
            ]
        )


    # UI components
    page.title = "Change Calculator"

    welcome_message = ft.Text(
        value="BGN to EUR change calculator",
        size=20
    )

    # The value of the total bill, default currency = EUR
    total_input = ft.TextField(
        label="Total",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=update_change,
        data="EUR"
    )

    # The value of the payment amount, default currency = BGN
    payment_amount_input = ft.TextField(
        label="Payment amount",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=update_change,
        data=DEFAULT_CURRENCY
    )

    # The calculated value of the change, default currency = EUR
    change_output = ft.TextField(
        label="Change",
        value="0.00",
        read_only=True,
        data="EUR"
    )


    # UI
    page.add(
        ft.Row(
            controls=[welcome_message]
        ),

        ft.Row(
            controls=[total_input]
        ),
        currency_row(total_input),

        ft.Row(
            controls=[payment_amount_input]
        ),
        currency_row(payment_amount_input),

        ft.Row(
            controls=[change_output]
        ),
        currency_row(change_output)
    )

    # counter = ft.Text("0", size=50, data=0)
    #
    # def increment_click(e):
    #     counter.data += 1
    #     counter.value = str(counter.data)
    #
    # page.floating_action_button = ft.FloatingActionButton(
    #     icon=ft.Icons.ADD, on_click=increment_click
    # )
    # page.add(
    #     ft.SafeArea(
    #         expand=True,
    #         content=ft.Container(
    #             content=counter,
    #             alignment=ft.Alignment.CENTER,
    #         ),
    #     )
    # )

if __name__ == '__main__':
    ft.run(main)
