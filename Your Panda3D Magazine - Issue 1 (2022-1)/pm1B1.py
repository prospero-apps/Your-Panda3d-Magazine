# file name: pm1B1.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import simplepbr

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set the color of the sky to a shade of blue.
        base.setBackgroundColor(.53, .81, .92)

        simplepbr.init()       
        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        # load UFO
        self.ufo = loader.loadModel('UFO/UFO.gltf')
        self.ufo.setPos(0, 50, 5)
        self.ufo.reparentTo(render)   

        # load terrain
        self.terrain = loader.loadModel('terrain/terrain.gltf')
        self.terrain.setPos(0, 50, -12)
        self.terrain.reparentTo(render) 

app = TestApp()
app.run()
