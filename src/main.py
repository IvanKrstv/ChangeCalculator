import flet as ft

from ChangeCalculator import ChangeCalculator

CURRENCIES = ("BGN", "EUR")
DEFAULT_CURRENCY = CURRENCIES[0] # BGN

def main(page: ft.Page):
    # currency_total = DEFAULT_CURRENCY
    # currency_payment_amount = DEFAULT_CURRENCY
    # currency_change = DEFAULT_CURRENCY

    def update_currency_bgn_to_eur(e, amount: ft.TextField):
        money_in_bgn = float(amount.value) if amount.value else 0.0

        money_in_eur = ChangeCalculator.convert_bgn_to_eur(money_in_bgn)
        amount.value = f"{money_in_eur:.2f}"
        page.update()

    def update_currency_eur_to_bgn(e, amount: ft.TextField):
        money_in_eur = float(amount.value) if amount.value else 0.0

        money_in_bgn = ChangeCalculator.convert_eur_to_bgn(money_in_eur)
        amount.value = f"{money_in_bgn:.2f}"
        page.update()

    # TODO: the 2 functions can be coded into 1 with dictionary?


    def update(e):
        total = float(total_input.value) if total_input.value else 0.0
        payment_amount = float(payment_amount_input.value) if payment_amount_input.value else 0.0

        result = payment_amount - total
        change_output.value = f"{result:.2f}"
        page.update()



    # UI components
    page.title = "Change Calculator"

    welcome_message = ft.Text(value="BGN to EUR change calculator")


    def create_bgn_button(textfield: ft.TextField):
        return ft.Button(
            content="BGN",
            on_click=lambda e: update_currency_eur_to_bgn(e, amount=textfield)
        )

    def create_eur_button(textfield: ft.TextField):
        return ft.Button(
            content="EUR",
            on_click=lambda e: update_currency_bgn_to_eur(e, amount=textfield)
        )


    # Row with BGN EUR buttons for the user to choose from
    # currency_row = ft.Row(
    #     controls=[
    #         create_bgn_button,
    #         create_eur_button
    #     ]
    # )


    total_input = ft.TextField(
        label="Total",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=update
    )

    payment_amount_input = ft.TextField(
        label="Payment amount",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=update
    )

    change_output = ft.TextField(
        label="Change",
        value="0.00",
        read_only=True
    )


    # UI
    page.add(
        ft.Row(
            controls=[welcome_message]
        ),

        ft.Row(
            # controls=[ft.TextField(label="Total", keyboard_type=ft.KeyboardType.NUMBER)]
            controls=[total_input]
        ),
        currency_row,

        ft.Row(
            # controls=[ft.TextField(label="Payment amount", keyboard_type=ft.KeyboardType.NUMBER)]
            controls=[payment_amount_input]
        ),
        currency_row,

        ft.Row(
            # controls=[ft.TextField(label="Change", value=str(1), read_only=True)]
            controls=[change_output]
        ),
        currency_row
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
