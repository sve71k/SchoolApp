from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDTextButton
from kivymd.uix.textfield import MDTextField


class SchoolApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return (
            MDScreen(
                MDBottomNavigation(


                    MDBottomNavigationItem(
                        MDLabel(
                            text='1',
                            halign='center',
                        ),
                        name='screen 1',
                        text='1',
                        icon='numeric-1-box-outline',
                    ),


                    MDBottomNavigationItem(
                        MDLabel(
                            text='2',
                            halign='center',
                        ),
                        name='screen 2',
                        text='2',
                        icon='numeric-2-box-outline',
                    ),


                    MDBottomNavigationItem(
                        MDLabel(
                            text='3',
                            halign='center',
                        ),
                        name='screen 3',
                        text='3',
                        icon='numeric-3-box-outline',
                    ),


                    MDBottomNavigationItem(
                        MDLabel(
                            text='4',
                            halign='center',
                        ),
                        name='screen 4',
                        text='4',
                        icon='numeric-4-box-outline',
                    ),


                    MDBottomNavigationItem(

                        MDTextField(
                            hint_text="Логин",
                            helper_text="Что-то",
                            pos_hint={"center_x": 0.5, "center_y": 0.6},
                            size_hint_x=0.5,
                        ),

                        MDTextField(
                            hint_text="Пароль",
                            helper_text="Что-то",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            size_hint_x=0.5,
                        ),

                        MDRectangleFlatButton(
                            text="Войти",
                            pos_hint={"center_x": 0.6, "center_y": 0.3},

                        ),

                        MDTextButton(
                            text="Создать аккаунт",
                            pos_hint={"center_x": 0.4, "center_y": 0.3},
                        ),

                        name='screen 5',
                        text='5',
                        icon='numeric-5-box-outline',
                    ),


                    selected_color_background="orange",
                    text_color_active="green",
                )
            )
        )


SchoolApp().run()