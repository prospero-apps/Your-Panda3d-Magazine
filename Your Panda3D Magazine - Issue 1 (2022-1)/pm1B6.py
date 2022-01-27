# file name: pm1B6.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.interval.IntervalGlobal import Sequence
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

        # create the single intervals
        posInterval1 = self.ufo.posInterval(3, (10, 50, 5)) 
        posInterval2 = self.ufo.posInterval(.5, (-8, 30, 2))
        posInterval3 = self.ufo.posInterval(2, (0, 20, 1))
        hprInterval = self.ufo.hprInterval(5, (0, 45, 0))                            
        
        # create and play the sequence 
        seq = Sequence(posInterval1, posInterval2, posInterval3, hprInterval)
        seq.start()

app = TestApp()
app.run()
