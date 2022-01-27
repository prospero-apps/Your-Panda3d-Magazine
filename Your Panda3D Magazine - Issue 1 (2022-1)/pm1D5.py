# file name: pm1D5.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr
from panda3d_kivy.app import App

# Kivy stuff
from kivy.uix.button import Button

# Kivy app
# change name to Gui1App
class Gui1App(App):
    def build(self):
        # Return a Button widget. Its implementation is
        # in the kv file.
        return Button()

# Panda3D app
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        display_region = self.win.make_display_region(.2, .8, .1, .4)

        # change name to Gui1App
        self.gui_app = gui_app = Gui1App(self, display_region)
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