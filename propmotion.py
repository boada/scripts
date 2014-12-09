
#######################################
# Computes the proper motion distance #
#######################################

def PropMotion(M1,L1,K1,function,p):
        if p == 1:
                file = open(function+'_'+str(M1)+'_'+str(L1)+'.txt','wt')
        PropD = []
        x =[]
        a=0
        if (L1 == 0.0):
                for z in drange(0,5,0.1):
                        x.append(z)
                        PropD.append(2.0*(2.0-M1*(1.0-z)-(2.0-M1)*math.sqrt(1.0+M1*z))/(math.pow(M1,2)*(1.0+z)))
                        if p ==1:
                                file.writelines(str(z)+" "+str(PropD[a])+"\n")
                        a+=1
                plot(x,PropD)
        else:
                args = (M1,L1,K1)
                for z in drange(0,5,0.1):
                        x.append(z)
                        result, err = integrate.quad(E_z,0,z,args)
                        PropD.append(result)
                        if p ==1:
                                file.writelines(str(z)+" "+str(result)+"\n")
                plot(x,PropD)
        if p ==1:
                file.close

        ylabel('Proper Motion Distance $D_m/D_h$')
        xlabel('Redshift z')
        if p!= 1:
                show()

