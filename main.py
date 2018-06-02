from trivia import trivia

from random import choice
from kivy.app import App
from kivy.uix.label import Widget


class Widgets(Widget):
    pass

class TriviaApp(App):
    def build(self):
        return Widgets()


TriviaApp().run()