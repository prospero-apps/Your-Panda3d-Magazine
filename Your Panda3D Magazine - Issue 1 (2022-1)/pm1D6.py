# file name: pm1D6.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr
from panda3d_kivy.app import App

# Kivy stuff
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class GuiLayout(BoxLayout):
    pass

# Kivy app
class Gui2App(App):
    
    x = NumericProperty()
    y = NumericProperty()
    z = NumericProperty()

    def build(self):
        return GuiLayout()

    def move_ufo(self, direction):
        self.ufo.move(direction)
        self.x = self.ufo.model.getX()
        self.y = self.ufo.model.getY()        

    def change_height(self, height):
        self.ufo.height(height)
        self.z = self.ufo.model.getZ()

# a separate class for our UFO
class UFO:
    def __init__(self):
        self.model = loader.loadModel('UFO/UFO.gltf')
        self.model.setPos(0, 50, 5)
        self.model.reparentTo(base.render) 

    def move(self, direction):
        if direction == 'north':
            self.model.setY(self.model.getY() + 1)
        elif direction == 'west':
            self.model.setX(self.model.getX() - 1)   
        elif direction == 'east':
            self.model.setX(self.model.getX() + 1)
        elif direction == 'south':
            self.model.setY(self.model.getY() - 1)  

    def height(self, height):
        self.model.setZ(height)          

# Panda3D app
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disable_mouse()
        
        display_region = self.win.make_display_region(0, .25, 0, 1)
        self.gui_app = gui_app = Gui2App(self, display_region)

        base.setBackgroundColor(.53, .81, .92)
        simplepbr.init()       
        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        self.ufo = UFO()
        self.terrain = loader.loadModel('terrain/terrain.gltf')
        self.terrain.setPos(0, 50, -12)
        self.terrain.reparentTo(render)    

        gui_app.ufo = self.ufo
        gui_app.x = self.ufo.model.getX()
        gui_app.y = self.ufo.model.getY()
        gui_app.z = self.ufo.model.getZ()
        gui_app.run()  

app = TestApp()
app.run()