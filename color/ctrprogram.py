from PIL import Image
import numpy as np
import math
import numpy
import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
i=0
j=1
for source in os.listdir(r"./"+"source"):
  i=i+1
  for target in os.listdir(r"./"+"target"):
    if (i == j) :
      pass
    else :
      if (j == 6):
        j=1
      else:
        j=j+1
      continue
   
    src=Image.open("source/"+source)
    tar=Image.open("target/"+target)
    rs,gs,bs=src.split()
    rt,gt,bt=tar.split()
    
    ar=np.array(rs).flatten()
    arrs, bins, patches = plt.hist(ar, bins=256,facecolor='r',edgecolor='r')
    ag=np.array(gs).flatten()
    aggs, bins, patches = plt.hist(ag, bins=256, facecolor='g',edgecolor='g')
    ab=np.array(bs).flatten()
    abbs, bins, patches = plt.hist(ab, bins=256, facecolor='b',edgecolor='b')

    art=np.array(rt).flatten()
    arrt, bins, patches = plt.hist(art, bins=256,facecolor='r',edgecolor='r')
    agt=np.array(gt).flatten()
    aggt, bins, patches = plt.hist(agt, bins=256, facecolor='g',edgecolor='g')
    abt=np.array(bt).flatten()
    abbt, bins, patches = plt.hist(abt, bins=256, facecolor='b',edgecolor='b')

    num=[]
    for index in range(0,256):
      num.append(index)

    arrs=arrs.tolist()
    aggs=aggs.tolist()
    abbs=abbs.tolist()
    arrt=arrt.tolist()
    aggt=aggt.tolist()
    abbt=abbt.tolist()

    def weighted_avg_and_std(values, weights):
        average = numpy.average(weights, weights=values)
        variance = numpy.average((weights-average)**2, weights=values)  # Fast and numerically precise
        return (average,math.sqrt(variance))

    mrs,stdrs=weighted_avg_and_std(arrs,num)
    mgs,stdgs=weighted_avg_and_std(aggs,num)
    mbs,stdbs=weighted_avg_and_std(abbs,num)
    mrt,stdrt=weighted_avg_and_std(arrt,num)
    mgt,stdgt=weighted_avg_and_std(aggt,num)
    mbt,stdbt=weighted_avg_and_std(abbt,num)

    pixel = src.load()
    mser=0
    mseg=0
    mseb=0

    for x in range(src.size[0]):
        for y in range(src.size[1]):
            r,g,b = pixel[x,y]
            rr=int((stdrt/stdrs)*(r-mrs)+mrt)
            rg=int((stdgt/stdgs)*(g-mgs)+mgt)
            rb=int((stdbt/stdbs)*(b-mbs)+mbt)
            if (rr>255): rr=255
            if (rg>255): rg=255
            if (rb>255): rb=255
            if (rr<0): rr=0
            if (rg<0): rg=0
            if (rb<0): rb=0
            pixel[x,y] = (rr,rg,rb)         #colortransfer後的

    src.save("ct-result\\"+"tr"+str(i)+".bmp") #colortransfer後的
    print("tr"+str(i)+".bmp already save")

    for x in range(src.size[0]):
        for y in range(src.size[1]):       
            r,g,b = pixel[x,y]              #colortransfer後的
            rr=int((stdrs/stdrt)*(r-mrt)+mrs)
            rg=int((stdgs/stdgt)*(g-mgt)+mgs)
            rb=int((stdbs/stdbt)*(b-mbt)+mbs)
            if(rr>255): rr=255
            if(rg>255): rg=255
            if(rb>255): rb=255
            if(rr<0): rr=0
            if(rg<0): rg=0
            if(rb<0): rb=0
            pixel[x,y] = (rr,rg,rb)         #recovery後的

    src.save("recov‐source\\"+"rs"+str(i)+".bmp")
    print("rs"+str(i)+".bmp already save")
    j=j+1
    
