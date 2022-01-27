# file name: pm1D3.py
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
        
        # create display region
        # We have to pass 4 values (ranging from 0 to 1) to create the region:
        # - the X position of the left side of the widget,
        # - the X position of the right side of the widget,
        # - the Y position of the bottom side of the widget,
        # - the Y position of the top side of the widget.
        # Here the region should start 20% into the width of the
        # window and extend up to 80% of the width. Vertically it 
        # should be from 10% to 40% of the height of the window.
        display_region = self.win.make_display_region(.2, .8, .1, .4)

        # pass display region to constructor
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