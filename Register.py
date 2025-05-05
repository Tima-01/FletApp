import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = "TimaAPP"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 450
    

    page.window_resizable = False
    page.update()

    def register(e):
        db = sqlite3.connect('test.db')
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            login TEXT,
            pass TEXT
        )""")
        cur.execute(f"""INSERT INTO users VALUES(NULL,'{user_login.value}','{user_pass.value}')""")
        db.commit()
        db.close()


        user_login.value = ''
        user_pass.value = ''
        btn_reg.text = 'Готово!'
        btn_reg.disabled = True
        page.update()

    def validate(e):
        btn_reg.text = 'Зарегистрироваться'
        if all([user_login.value, user_pass.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
        page.update()

    def auth_user(e):
        db = sqlite3.connect('test.db')
        cur = db.cursor()

        cur.execute(f"""SELECT * FROM users WHERE login ='{user_login.value}' AND pass = '{user_pass.value}'""")

        if cur.fetchone() != None:
            user_login.value = ''
            user_pass.value = ''
            btn_auth.text = 'Готово!'
            btn_auth.disabled = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Неверные данные!'))
            page.snack_bar.open = True
            page.add(page.snack_bar)
            page.update()
        db.commit()
        db.close()




    user_login = ft.TextField(label='Введите логин', width=200, on_change = validate)
    user_pass = ft.TextField(label='Введите пароль',password=True, width=200,on_change = validate)
    btn_reg= ft.OutlinedButton(text='Зарегистрироваться', width = 200, on_click = register, disabled = True)
    btn_auth = ft.OutlinedButton(text='Авторизовать', width=200, on_click=auth_user, disabled=True)

    page.update()

    panel_registration =ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Регистрация'),
                        user_login,
                        user_pass,
                        btn_reg
                    ]
                )
            ], alignment = ft.MainAxisAlignment.CENTER
        )
    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Авторизация'),
                    user_login,
                    user_pass,
                    btn_auth
                ]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )


    def navigate(e):
        print(page.navigation_bar.selected_index)

    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationBarDestination(icon=ft.Icons.VERIFIED_USER, label = "Регистрация"),
            ft.NavigationBarDestination(icon=ft.Icons.VERIFIED_USER_OUTLINED, label="Авторизация")
       ],on_change = navigate
    )

    page.add(
        panel_auth
    )
ft.app(target=main, view=ft.AppView.FLET_APP)

