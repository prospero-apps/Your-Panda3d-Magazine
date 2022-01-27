# file name: pm1B2.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, Point3
import simplepbr

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
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

        # create interval
        posInterval = self.ufo.posInterval(3, 
                           Point3(10, 50, 5), 
                           startPos=Point3(0, 50, 5))
        
        # start interval
        posInterval.start()

app = TestApp()
app.run()
