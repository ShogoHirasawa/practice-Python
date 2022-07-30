from turtle import *
def come(x,y):
  (xx,yy) = pos()
  newxy = ((xx+y)/2,(yy+y)/2)
  print(x,y)
  goto(newxy)
onscreenclick(come)
done()