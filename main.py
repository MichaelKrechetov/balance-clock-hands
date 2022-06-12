from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.graphics import Triangle
from kivy.uix.slider import Slider


class MyGrid(Widget):
    square_long = ObjectProperty(None)
    square_short = ObjectProperty(None)
    length_long = ObjectProperty(None)
    length_short = ObjectProperty(None)
    density = ObjectProperty(None)
    thickness = ObjectProperty(None)
    weight = ObjectProperty(None)
    distance = ObjectProperty(None)

    def balance(self):
        pass

    def draw(self):
        print("test1")



class BalanceClockHands(App):
    def build(self):

        return MyGrid()



if __name__ == "__main__":
    BalanceClockHands().run()

