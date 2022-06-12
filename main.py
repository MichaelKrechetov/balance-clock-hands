from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyGrid(Widget):
    pass


class BalanceClockHands(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    BalanceClockHands().run()

