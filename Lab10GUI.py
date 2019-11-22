import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import backend as dao
kivy.require("1.11.1")


#dao.search_table("vendor", "vendor_name", "Hulkey Fasteners")


class MainWindow(Screen):
    n = ObjectProperty(None)
    current = "main"

    def vendor(self):
        sm.current = "vendor"

    def orderButton(self):
        sm.current = "orders"
    
    def product(self):
        sm.current = "product"


class VendorWindow(Screen):
    def doSomething(self):
        print("lol")

class OrderWindow(Screen):
    def doSomething(self):
        print("lul")

class ProductWindow(Screen):
    def doSomething(self):
        print("omegalul")

class LineWindow(Screen):
    def doSomething(self):
        print("hyperomegalul")


class WindowManager(ScreenManager):
    pass

sm = WindowManager()
kv = Builder.load_file("lab10gui.kv")

screens = [MainWindow(name="main"), VendorWindow(name="vendors"),OrderWindow(name="orders"),
 ProductWindow(name="products"), LineWindow(name="lines")]
for screen in screens:
    sm.add_widget(screen)

class MainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MainApp().run()
