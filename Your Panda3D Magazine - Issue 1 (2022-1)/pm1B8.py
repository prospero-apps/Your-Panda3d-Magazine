# file name: pm1B8.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.interval.IntervalGlobal import Sequence, Parallel
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

        # sequence 1
        posInterval1 = self.ufo.posInterval(3, (10, 50, 5)) 
        posInterval2 = self.ufo.posInterval(2, (0, 20, 1))
        hprInterval1 = self.ufo.hprInterval(5, (0, 45, 0))  
        seq1 = Sequence(posInterval1, posInterval2, hprInterval1)
        
        # parallel 1
        posInterval3 = self.ufo.posInterval(1, (2, 20, 1))
        hprInterval2 = self.ufo.hprInterval(1, (0, 15, 15))        
        par1 = Parallel(posInterval3, hprInterval2)

        # parallel 2
        posInterval4 = self.ufo.posInterval(1, (0, 20, -3))
        hprInterval3 = self.ufo.hprInterval(1, (0, -15, -15))        
        par2 = Parallel(posInterval4, hprInterval3)

        # sequence 2 (plays parallel 1 and then parallel 2)
        seq2 = Sequence(par1, par2)

        # sequence 3 (plays sequence 1, then sequence 2 and then
        # some other single intervals)
        hprInterval4 = self.ufo.hprInterval(2, (360, 0, 0))
        hprInterval5 = self.ufo.hprInterval(1, (720, 0, 0))
        posInterval5 = self.ufo.posInterval(1, (150, 500, 30))
        posInterval6 = self.ufo.posInterval(.25, (300, 500, 30))
        seq3 = Sequence(seq1, seq2, hprInterval4, hprInterval5, 
                        posInterval5, posInterval6)

        seq3.start()

app = TestApp()
app.run()
