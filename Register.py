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

        db.close()
        db.commit()

        user_login.value = ''
        user_pass.value = ''
        btn_reg.text = 'Готово!'
        btn_reg.disabled = True
        page.update()

    def validate(e):
        btn_reg.text = 'Зарегистрироваться'
        if all([user_login.value, user_pass.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()
    user_login = ft.TextField(label='Введите логин', width=200, on_change = validate)
    user_pass = ft.TextField(label='Введите пароль',password=True, width=200,on_change = validate)
    btn_reg= ft.OutlinedButton(text='Зарегистрироваться', width = 200, on_click = register, disabled = True)
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
    page.add(
        panel_registration
    )
ft.app(target=main)