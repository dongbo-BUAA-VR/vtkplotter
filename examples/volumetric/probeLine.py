# Intersect a vtkImageData (voxel dataset) with planes
#
from vtkplotter import show, loadImageData, probeLine, vector

img = loadImageData('data/embryo.slc')

pos = img.GetCenter()

lines=[]
for i in range(60): # probe scalars on 60 parallel lines
    step = (i-30)*2
    p1, p2 = pos+vector(-100, step,step), pos+vector(100, step,step)
    a = probeLine(img, p1, p2, res=200)
    a.alpha(0.5).lineWidth(9)
    lines.append(a)
    #print(a.scalars(0)) # numpy scalars can be access here
    #print(a.scalars('vtkValidPointMask')) # the mask of valid points

show(lines, axes=4, verbose=0)