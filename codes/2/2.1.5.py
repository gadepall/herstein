
#Code by GVV Sharma
#August 8, 2022
#released under GNU GPL
#Using sympy to verify the properties of a group 
#Herstein 2.1.5


import sys                                          #for path to external scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts
#sys.path.insert(0, '/data/data/com.termux/files/home/storage/shared/github/training/math/codes/CoordGeo')        #path to my scripts
#sys.path += ['/data/data/com.termux/files/home/storage/shared/github/training/math/codes/CoordGeo','/data/data/com.termux/files/home/arch/home/user/miniforge3/envs/my-env']

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy.linalg as LA
import sympy as smp
from sympy.abc import x,y


#local imports
#from line.funcs import *
#
#from triangle.funcs import *
#from conics.funcs import circ_gen


#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if

#Ellipse parameters

#Sympy version

#Inputs
#usym = smp.Rational(1,2)*smp.Matrix(([-44,-58]))
#Vsym = smp.Matrix(([14, -2],[-2,11]))
f = smp.Matrix(([-1, 0],[0,1]))
g = smp.Matrix(([0, -1],[1,0]))
#fsym = smp.Matrix(([71]))

##Eigenvalues
#Psym, Dsym = Vsym.diagonalize()
#Psym=Psym/smp.sqrt((Psym.T@Psym)[0,0])
#psym1 = Psym.col(0)
#psym2 = Psym.col(1)
#
#
##Vertex
#Vinv = Vsym.inv()
#csym = -Vinv@usym
#csymlatex = smp.latex(csym)
#
##axes lengths
#f0sym = usym.T@Vinv@usym- fsym
#a = smp.sqrt(f0sym/Dsym[0,0])
#b = smp.sqrt(f0sym/Dsym[1,1])
print(smp.latex(f.inv()),smp.latex(g.inv()))
#print(F**2,G**4)
#print(smp.latex(g@f))
#
