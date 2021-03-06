from __future__ import division, print_function
from random import uniform as u
from vtkplotter import printc, ProgressBar, Plotter, plane

N = 10      # nr of particles along axis
s = 0.01    # random step size

scene = Plotter(verbose=0, axes=0)

scene.add(plane(pos=[.44,.44,-.1], texture='wood7'))

for i in range(N):              # generate a grid of points
    for j in range(N): 
        for k in range(N):
            p = [i/N, j/N, k/N]
            scene.point(p, c=p) # color point by its own position

pb = ProgressBar(0, 80, c='red')
for t in pb.range():            # loop of 400 steps
    pb.print()   
    
    for i in range(1, N*N*N):   # for each particle
        actor = scene.actors[i]
        r = [u(-s,s), u(-s,s), u(-s,s)] # random step
        p = actor.pos()         # get point position
        q = p + r               # add the noise
        if q[2]<0: q[2] *= -1   # if bounce on the floor
        actor.pos(q)            # set its new position
    scene.camera.Azimuth(.5)
    scene.camera.Roll(-.5)
    scene.render()

scene.show(resetcam=0)
