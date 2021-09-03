from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import DataBase

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class CreateAccountWindow(Screen):

    namee = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def reset(self):
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "main"

    def submit(self):
        if self.namee.text != "":
            if self.password != "":
                db.add_user(self.password.text, self.namee.text, self.email)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()


class WindowManager(ScreenManager):
    pass


sm = WindowManager()
kv = Builder.load_file("my.kv")
db = DataBase("user.txt")

screens = [SecondWindow(name="second"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
