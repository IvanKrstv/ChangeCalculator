import flet as ft


def main(page: ft.Page):
    page.title = "Change Calculator"
    welcome_message = ft.Text(value="BGN to EUR change calculator")
    currency_row = ft.Row(
            controls=[
                ft.Button(content="BGN"),
                ft.FilledButton(content="EUR")
            ]
        )

    page.add(
        ft.Row(
            controls=[welcome_message]
        ),

        ft.Row(
            controls=[ft.TextField(label="Total")]
        ),
        currency_row,

        ft.Row(
            controls=[ft.TextField(label="Payment amount")]
        ),
        currency_row,

        ft.Row(
            controls=[ft.TextField(label="Change", value=str(1), read_only=True)] #TODO logic for value
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
