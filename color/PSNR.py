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
for resource in os.listdir(r"./"+"recov‐source"):
  i=i+1
  for source in os.listdir(r"./"+"source"):
    if (i == j) :
      pass
    else :
      if (j == 6):
        j=1
      else:
        j=j+1
      continue
   
    resrc=Image.open("recov‐source/"+resource)
    src=Image.open("source/"+source)

    #src1=Image.open("source/"+source)
    mser=0
    mseg=0
    mseb=0
    pixel = resrc.load()
    pixel1 = src.load()
    for x in range(src.size[0]):
        for y in range(src.size[1]):       
            r,g,b = pixel[x,y]              #recovery後的
            r1,g1,b1 = pixel1[x,y]          #原本的source
            mser=mser+(r-r1)*(r-r1)
            mseg=mseg+(g-g1)*(g-g1)
            mseb=mseb+(b-b1)*(b-b1)

 	#图像的行数
    height = src.size[0]
    #图像的列数
    width = src.size[1]
    MSE = (mser+mseg+mseb)/(height * width * 3)   
    PSNR = 10*math.log ( (255.0*255.0/(MSE)) ,10)

    # 開啟輸出的 CSV 檔案
    with open('PSNR‐result\\PSNR‐result'+str(i)+'.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        writer.writerow(["PSNR"])
        writer.writerow([PSNR])

    j=j+1