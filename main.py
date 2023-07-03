from kivymd.app import MDApp
from kivy.lang  import Builder


class ThMainApp(MDApp):
    def build(self):
        return Builder.load_file('ThMainPage.kv')

if __name__ == '__main__':
    ThMainApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
