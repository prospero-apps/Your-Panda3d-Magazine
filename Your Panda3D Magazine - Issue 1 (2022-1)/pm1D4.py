# file name: pm1D4.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr
from panda3d_kivy.app import App

# Kivy stuff
# We don't need the Button class here, but we need the 
# Builder class to load the Kivy string.
from kivy.lang import Builder

# Here's the Kivy string where we define the button.
kivy_code = r'''
Button:
    text: 'UFO'
    font_size: 80
    color: 1, 0, 0, 1
'''

# Kivy app
class GuiApp(App):
    def build(self):
        # Now we load the Kivy string.
        return Builder.load_string(kivy_code)

# Panda3D app
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        display_region = self.win.make_display_region(.2, .8, .1, .4)
        self.gui_app = gui_app = GuiApp(self, display_region)
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