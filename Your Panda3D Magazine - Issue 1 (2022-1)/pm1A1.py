# file name: pm1A1.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        self.ufo = loader.loadModel("UFO")
        self.ufo.setPos(0, 50, 0)
        self.ufo.reparentTo(render)   

app = TestApp()
app.run()
