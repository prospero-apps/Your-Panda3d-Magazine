# file name: pm1B7.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.interval.IntervalGlobal import Parallel
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
        posInterval = self.ufo.posInterval(10, (10, 50, 5))
        hprInterval = self.ufo.hprInterval(5, (0, 45, 0))
        scaleInterval = self.ufo.scaleInterval(5, (1, 3, 1))                    
        
        # create and play the parallel 
        par = Parallel(posInterval, hprInterval, scaleInterval)
        par.start()

app = TestApp()
app.run()
