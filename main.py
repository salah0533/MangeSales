from kivy.core.window import Window
from kivy.graphics import Color, Line, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.lang  import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy_gradient import Gradient
from kivy.utils import get_color_from_hex

# class MyCard(BoxLayout):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         self.width = Window.size[0]
#         self.height = Window.size[1]
#         self.add_gradiant()


#     def interpolate_color(self,color_a, color_b, t):
#         r = int(color_a[0] + (color_b[0] - color_a[0]) * t)
#         g = int(color_a[1] + (color_b[1] - color_a[1]) * t)
#         b = int(color_a[2] + (color_b[2] - color_a[2]) * t)
#         return (r/255, g/255, b/255,1)
#     def add_gradiant(self):
#         color_a = (244, 91, 128)
#         color_b = (244, 0, 44)

#         increase_rate = 1 / self.width

#         for sep in range(self.width):
#             t = sep / self.width
#             interpolated_color = self.interpolate_color(color_b, color_a, t)
#             print(interpolated_color)
#             self.canvas.add(Color( rgba = interpolated_color ))
#             self.canvas.add(Line(points=[sep, 0, sep, self.height], width=1))



class ThMainApp(MDApp):
    def build(self):
        return Builder.load_file('ThMainPage.kv')



if __name__ == '__main__':
    ThMainApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
