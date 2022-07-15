street = ["三条河原町", "三条烏丸", "三条堀川"]
street2 = ['四条堀川', '四条烏丸', '四条河原町']
street3 = ['五条堀川', '五条烏丸', '五条河原町']


for i in range(len(street)):
 if i < len(street)-1:
  print(street[i],end=", ")  
 else:
  print(street[i],end="\n") 

for j in range(len(street2)):
 if j < len(street2)-1:
  print(street2[j],end=", ")  
 else:
  print(street2[j],end="\n") 

for n in range(len(street3)):
 if n < len(street3)-1:
  print(street3[n],end=", ")  
 else:
  print(street3[n],end="\n") 