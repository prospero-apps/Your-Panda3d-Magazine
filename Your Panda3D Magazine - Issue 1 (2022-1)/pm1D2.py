# file name: pm1D2.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr
from panda3d_kivy.app import App

# Kivy stuff
from kivy.uix.button import Button

# Kivy app
class GuiApp(App):
    def build(self):
        return Button(text='UFO', font_size=80, 
                     color=(1, 0, 0, 1))

# Panda3D app
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

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