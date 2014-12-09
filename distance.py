#!/usr/bin/python

# Copyright (C) 2011  Steven Boada

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math
import sys
from pylab import *
from scipy import integrate, inf

def main(argv):

	if (len(sys.argv) <= 3):
		print "This function requires options."
		print "Use '--h' or '--help' for usage"
		sys.exit(1)	
	M1 = eval(sys.argv[2]) #omega_m
	L1 = eval(sys.argv[3]) #omega_lambda
	K1 = 1.0 - M1 - L1 #omega_k

	function = globals().get(sys.argv[1])
	if hasattr(function, '__call__'):
    	    function(M1,L1,K1,sys.argv[1],0)
	else:
		print "You have specified a function that doesn't exist."
		print "Use '--h' or '--help' for usage."

########################################
# Same as a 'for' loop but accepts and #
# returns floating point numbers.      #
########################################

def drange(start,stop,step):
        r=start
        while r<stop:
                yield r
                r+=step
######################################
# Used for all distance calculations #
######################################

def E_z(z,M1,L1,K1):
        return math.pow(math.sqrt(M1*math.pow((1.0+z),3)+K1*math.pow((1.0+z),2)+L1),-1.0)

###############################
# Used for Lookback time only #
###############################

def E_z2(z,M1,L1,K1):
        return math.pow((1.0+z)*math.sqrt(M1*math.pow((1.0+z),3)+K1*math.pow((1.0+z),2)+L1),-1.0)

#######################################
# Computes the proper motion distance #
#######################################

def PropMotion(M1,L1,K1,function,p):
	z=1.5
	if (L1 == 0.0):
		PropD =2.0*(2.0-M1*(1.0-z)-(2.0-M1)*math.sqrt(1.0+M1*z))/(math.pow(M1,2)*(1.0+z))
	else:
		args = (M1,L1,K1)
		result, err = integrate.quad(E_z,0,z,args)
		PropD= result
    
        return PropD

##########################################
# Computes the Angular Diameter Distance #
##########################################

def AngDiam(M1,L1,K1,function,p):
	if p == 1:
		file = open(function+'_'+str(M1)+'_'+str(L1)+'.txt','wt')
	AngD= []
	x=[]
	a=0
	if (L1 == 0.0):
	        for z in drange(0,5,0.1):
	                x.append(z)
	                AngD.append(2.0*(2.0-M1*(1.0-z)-(2.0-M1)*math.sqrt(1.0+M1*z))/(math.pow(M1,2)*math.pow((1.0+z),2)))
			if p ==1:
	                	file.writelines(str(z)+" "+str(AngD[a])+"\n")
	                a+=1
			plot(x,AngD)
	else:
	        args = (M1,L1,K1)
	        for z in drange(0,5,0.1):
	                x.append(z)
	                result, err = integrate.quad(E_z,0,z,args)
	                AngD.append(result/(1.0+z))
			if p ==1:
	                	file.writelines(str(z)+" "+str(result/(1.0+z))+"\n")
	                plot(x,AngD)
	if p ==1:
		file.close

	xlabel('Redshift $z$')
	ylabel('Angular Diameter Distance $D_a/D_h$')
	if p!= 1:
		show()

################################
# Computes the Comoving Volume #
################################

def ComovingVol(M1,L1,K1,function,p):
	if p == 1:
		file = open(function+'_'+str(M1)+'_'+str(L1)+'.txt','wt')
	Comov = []
	x = []
	a=0
	if (L1 == 0.0):
	        for z in drange(0,5,0.1):
	                x.append(z)
	                PropD = 2.0*(2.0-M1*(1.0-z)-(2.0-M1)*math.sqrt(1.0+M1*z))/(math.pow(M1,2)*(1.0+z))
	                Comov.append(math.pow(PropD,2)/math.sqrt(M1*math.pow((1.0+z),3)))
			if p ==1:
	                	file.writelines(str(z)+" "+str(Comov[a])+"\n")
	   		a+=1
			plot(x,Comov)
	else:
	        args = (M1,L1,K1)
	        for z in drange(0,5,0.1):
	                x.append(z)
	                result, err = integrate.quad(E_z,0,z,args)
	                DA = result/(1.0+z)
	                Comov.append((math.pow((1.0+z),2)*math.pow(DA,2))/math.pow(E_z(z,M1,L1,K1),-1.0))
			if p ==1:
	                	file.writelines(str(z)+" "+str(Comov[a])+"\n")
			a+=1
	        plot(x,Comov)
	if p ==1:
		file.close

	ylabel('Comoving Volume Element')
	xlabel('Redshift $z$')
	if p!= 1:
		show()

####################################
# Computes the Luminosity Distance #
####################################

def LumDist(M1,L1,K1,function,p):
	if p == 1:
		file = open(function+'_'+str(M1)+'_'+str(L1)+'.txt','wt')
	LumD = []
	x=[]
	a=0
	if (L1 == 0.0):
	        for z in drange(0,5,0.1):
	                x.append(z)
	                LumD.append(2.0*(2.0-M1*(1.0-z)-(2.0-M1)*math.sqrt(1.0+M1*z))/(math.pow(M1,2)))
			if p ==1:
	                	file.writelines(str(z)+" "+str(LumD[a])+"\n")
	   		a+=1
		plot(x,LumD)
	else:
	        args = (M1,L1,K1)
	        for z in drange(0,5,0.1):
	                x.append(z)
	                result, err = integrate.quad(E_z,0,z,args)
	                LumD.append(result*(1.0+z))
			if p ==1:
	                	file.writelines(str(z)+" "+str(result*(1.0+z))+"\n")
	        plot(x,LumD)
	if p ==1:
		file.close

	ylabel('Luminosity Distance $D_L/D_H$')
	xlabel('Redshift $z$')
	if p!= 1:
		show()

	return 0

######################################
# Computes the Lookback time and the #
# corresponding age of the universe  #
######################################

def Lookback(M1,L1,K1,function,p):
	if p == 1:
		file = open(function+'_'+str(M1)+'_'+str(L1)+'.txt','wt')
	LB=[]
	LB2=[]
	x=[]
	args = (M1,L1,K1)
	for z in drange(0,5,0.1):
	        x.append(z)
	        result, err = integrate.quad(E_z,0.0,z,args) # Lookback
	        result2, err = integrate.quad(E_z2,z,inf,args) # Age of Universe
	        LB.append(result)
	        LB2.append(result2)
		if p ==1:
	        	file.writelines(str(z)+" "+str(result)+" "+str(result2)+"\n")
	
	if p ==1:
		file.close
	plot(x,LB)
	plot(x,LB2)
	print LB[-1], LB2[-1]
	ylabel('Lookback Time $T_L/T_H$')
	xlabel('Redshift $z$')
	if p!= 1:
		show()

if __name__ == "__main__":
	sys.exit(main(sys.argv))
