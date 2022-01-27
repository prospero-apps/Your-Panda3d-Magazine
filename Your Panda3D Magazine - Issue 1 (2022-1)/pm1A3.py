# file name: pm1A3.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

# We need to import simplepbr.
import simplepbr

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # We must call simplepbr's init method here.
        simplepbr.init()

        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        self.ufo = loader.loadModel("UFO.gltf")
        self.ufo.setPos(0, 50, 0)
        self.ufo.reparentTo(render)   

app = TestApp()
app.run()
