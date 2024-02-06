from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class MyApp(App):

    def build(self):
        label = Label(text= "MyApp")

        return label



if __name__ == '__main__':
    MyApp().run()