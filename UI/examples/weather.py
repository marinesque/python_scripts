import flet as ft

def main(page: ft.Page):
    page.title = "Flet app"
    page.theme_mode = 'dark' # or light
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # all in the center

    user_label = ft.Text('Info', color='#fafafa')
    user_text = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)

    def get_info(event):
        user_label.value = user_text.value
        page.update()

    page.add(
        ft.Row( # список кнопок
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),
                ft.Icon(ft.icons.BACK_HAND),
                ft.ElevatedButton(text='Click me', on_click=get_info),
                ft.OutlinedButton(text='Click me too', on_click=get_info),
                ft.Checkbox(label='Are you sure?', value=True)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(  # список кнопок
            [
                user_label,
                user_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# ft.app(target = main) #десктоп приложение
ft.app(target = main, view=ft.AppView.WEB_BROWSER) #веб-приложение
