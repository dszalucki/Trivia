from trivia import trivia

from random import choice
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class TriviaAppBoxLayout(BoxLayout):
    def showTrivia(self):
        output = choice(trivia)
        self.ids.result.text = output

class TriviaApp(App):
    def build(self):
        return TriviaAppBoxLayout()


TriviaApp().run()