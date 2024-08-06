import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent


def main(page: ft.Page):

    # window settings
    page.title = 'Signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.resizable = False

    # window objects
    text_username = TextField(             # user field
                        label='Username', 
                        text_align=ft.TextAlign.LEFT, 
                        width=200)
    text_password = TextField(             # pass field
                        label='Password', 
                        text_align=ft.TextAlign.LEFT, 
                        width=200, password=True)
    checkbox_signup = Checkbox(            # agreement box
                        label='I agree to paying 1b dollars to the owner', 
                        value=False)
    button_submit = ElevatedButton(        # submit button
                        text='Submit', 
                        width=200, 
                        disabled=True)

    # check inputs to enable submit button
    def validate(e: ControlEvent):
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else: 
            button_submit.disabled = True  
        page.update()                               # set button -> refresh window

    # submit button is pressed
    def submit(e: ControlEvent):
        print('Username: ', text_username.value)    # display data on terminal
        print('Password: ', text_password.value)    # display data on terminal
        page.clean()                           
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}',size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # call functions on onject change
    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_signup.on_change = validate 
    button_submit.on_click = submit

    # add objects
    page.add(
        Row(
            controls=[Column([text_username, text_password, checkbox_signup, button_submit])],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ) 


# start flet app with main()
ft.app(target=main)
