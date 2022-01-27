# file name: pm1D1.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr

# Make sure to import the App class before importing
# any Kivy-related stuff
from panda3d_kivy.app import App

# Kivy stuff
from kivy.uix.label import Label

# Create a subclass of App with the build method that
# returns the root widget, so in our case the label.
class GuiApp(App):
    def build(self):
        return Label(text='UFO', font_size=80, 
                     color=(1, 0, 0, 1))

# Create the Panda3D app class, so the class that 
# inherits from ShowBase, just like in any Panda3D app.
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Instantiate and run the Kivy app class
        # inside the Panda3D constructor.
        self.gui_app = gui_app = GuiApp(self)
        gui_app.run()

        base.setBackgroundColor(.53, .81, .92)
        simplepbr.init()       
        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        self.ufo = loader.loadModel('UFO/UFO.gltf')
        self.ufo.setPos(0, 50, 5)
        self.ufo.reparentTo(render)   

        self.terrain = loader.loadModel('terrain/terrain.gltf')
        self.terrain.setPos(0, 50, -12)
        self.terrain.reparentTo(render)      

app = TestApp()
app.run()