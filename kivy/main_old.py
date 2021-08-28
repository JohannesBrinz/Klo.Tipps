import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGrid(GridLayout):
    def __init__(self, **kwargs):           #kwargs for keywords, ** ass many as I want
        super(MyGrid, self).__init__(**kwargs)          #calls the init of GridLayout
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label (text = "Name: "))
        self.name = TextInput(multiline=False)      #only one lnie
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label (text = "First Name: "))
        self.firstname = TextInput(multiline=False)      #only one lnie
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label (text = "Email: "))
        self.email = TextInput(multiline=False)      #only one lnie
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)


        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        firstname = self.firstname.text
        email = self.email.text

        print("Name: ", name, "\nFirst Name: ", firstname, "\nEmail: ", email)
        self.name.text = ""                 #clear things
        self.firstname.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
