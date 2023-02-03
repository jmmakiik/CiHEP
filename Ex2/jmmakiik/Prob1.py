#!/usr/bin/env python

from multiprocessing import Process
import subprocess

path = "~/CiHEP/Ex2/jmmakiik/Prob1" #Path has to be changed depending on where the files are (removing/replacing /CiHEP part for example)

def hello(num):
    output = open("hellopy_%s"%num, "w")
    subprocess.run(path + " "+ num, shell=True, stdout=output)
    output.close()

for i in range(10):
    number = str(i+1)
    p = Process(target=hello, args={number,})
    p.start()
    p.join()
    
