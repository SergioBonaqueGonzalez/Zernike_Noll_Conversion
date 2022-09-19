"""
Created on Tue May 29 15:03:25 2018

@author: Dr. Sergio Bonaque-Gonzalez
Optical Engineer.
sergio.bonaque.gonzalez@gmail.com
"""
import numpy
from sympy.solvers import solve
from sympy import Symbol

def noll_to_ANSI(j):
    n = 0
    j1 = j-1
    while (j1 > n):
        n += 1
        j1 -= n
        
    m = (-1)**j * ((n % 2) + 2 * int((j1+((n+1)%2)) / 2.0 ))
    return (('position',n, m))
    
    

def OSA_to_ANSI(j):
    n = 1
    j1 = j-1
    m1=Symbol('m1')
    while (j1 > n):
        n += 1
        j1 -= n
    m=solve(((n*(n+2)+m1)/2)-j,(m1))  
        
    return(('position',n,m[0]))
    

def createlists(zermax):
    i=1
    OSA=[0]
    Noll=[0]
    
    while i<=zermax:
        OSA.append(OSA_to_ANSI(i))
        Noll.append(noll_to_ANSI(i))
        i +=1
    Noll.append(noll_to_ANSI(i)) #As Noll do not starts in zero, we need one more.
    return(OSA,Noll)
    

OSA,NOLL=createlists(14)
OSA[0]=('position', 0, 0)
NOLL[0]=[]
equivalent_OSA_in_Noll=numpy.zeros(len(OSA)) 
for i in range(0,len(OSA)):
    equivalent_OSA_in_Noll[i]=int(NOLL.index(OSA[i]))

equivalent_Noll_in_OSA=numpy.zeros(len(NOLL)) 
for i in range(1,len(NOLL)):
    equivalent_Noll_in_OSA[i]=int(OSA.index(NOLL[i]))
equivalent_Noll_in_OSA[0]=None


    
def ANSItoNOLL(index):
   return int(equivalent_OSA_in_Noll[index])

def NOLLtoANSI(index):
   return int(equivalent_Noll_in_OSA[index])
