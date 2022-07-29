from turtle import *

n = 7 #n角形にするかを決める
a = 180 -(180/n) #内角の計算

for i in range(n):
  forward(100)
  left(a)
done()

