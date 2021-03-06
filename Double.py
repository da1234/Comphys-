from matplotlib import pyplot as plt 
import numpy as np 


class Double:
    
    
    def __init__(self,R,G,step,time,Egraph):        
        self.RK4(R,G,step,time,Egraph)
                        
    def Energy_plot(self,w,R,v,o,y,t,Egraph):        
        energies = np.zeros(t.size)
        KEs = np.zeros(t.size)
        PEs = np.zeros(t.size)        
        for i in range(t.size):               
            KE = 0.5*w[i]**2 + 0.5*R*(w[i]**2 + v[i]**2 + 2*w[i]*v[i]*np.cos(o[i]-y[i]))
            PE = (1-np.cos(o[i])) + R*(1-np.cos(o[i])) +R*(1-np.cos(y[i]))
            energy = KE +PE            
            energies[i] = energy
            KEs[i] = KE
            PEs[i] = PE                    
        energyChanges = [0]
        for i in range(1, len(energies)):
            energyChange = energies[i] - energies[i-1]
            energyChanges.append(energyChange)                
        if Egraph == "energy_changes":         
            plt.figure()
            plt.plot(t,energyChanges,'.-')
            plt.title("energy changes")
            plt.xlabel("time")
            plt.ylabel("Energy change")
            plt.grid()
            plt.show()            
        elif Egraph == "energy_values":        
            plt.figure()
            plt.plot(t, energyChanges, 'y')
            plt.plot(t, np.zeros(t.size), 'r')
            plt.title('Energy')
            plt.xlabel('Time')
            plt.ylabel('Energy values')
            plt.grid()        

    def RK4(self,R,G,step,time,Egraph):        
        h =step
        t= np.arange(0,time,h)
        o = np.full(t.size, 0.01)
        y = np.zeros(t.size)
        w = np.zeros(t.size)
        v = np.zeros(t.size)                
        for i in range(1, t.size):            
            ko1 = w[i-1]
            ky1= v[i-1]
            kw1 = -(R+1)*o[i-1] + y[i-1]*R -G*w[i-1]
            kv1 = (R+1)*o[i-1]- (R+1)*y[i-1] + G*(1-(R**-1))*w[i-1] - (G*(R**-1))*v[i-1]            
            o1 = o[i-1] + h*ko1/2
            y1 = y[i-1] + h*ky1/2
            w1 = w[i-1] + h*kw1/2
            v1 = v[i-1] + h*kv1/2            
            ko2 = w1
            ky2= v1
            kw2 = -(R+1)*o1 + y1*R -G*w1
            kv2 = (R+1)*o1- (R+1)*y1 + G*(1-(R**-1))*w1 - (G*(R**-1))*v1            
            o2 = o[i-1] + h*ko2/2
            y2 = y[i-1] + h*ky2/2
            w2 = w[i-1] + h*kw2/2
            v2 = v[i-1] + h*kv2/2            
            ko3 = w2
            ky3= v2
            kw3 = -(R+1)*o2 + y2*R -G*w2
            kv3 = (R+1)*o2- (R+1)*y2 + G*(1-R**-1)*w2 - (G*R**-1)*v2            
            o3 = o[i-1] + h*ko3
            y3 = y[i-1] + h*ky3
            w3 = w[i-1] + h*kw3
            v3 = v[i-1] + h*kv3            
            ko4 = w3
            ky4= v3
            kw4 = -(R+1)*o3 + y3*R -G*w3
            kv4 = (R+1)*o3 - (R+1)*y3 + G*(1-R**-1)*w3 - (G*R**-1)*v3            
            o[i] = o[i-1] + h/6 * (ko1 + 2*ko2 + 2*ko3 + ko4)
            y[i] = y[i-1] + h/6 * (ky1 + 2*ky2 + 2*ky3 + ky4)
            w[i] = w[i-1] + h/6 * (kw1 + 2*kw2 + 2*kw3 + kw4)
            v[i] = v[i-1] + h/6 * (kv1 + 2*kv2 + 2*kv3 + kv4)                                    
        plt.figure()
        plt.plot(t,o,'--')
        plt.plot(t,y)
        plt.title("RK4 with R="+str(R)+", h= "+str(h) + " and G="+ str(G))
        plt.xlabel("time")
        plt.ylabel("angle")
        plt.grid()
        plt.show()                 
        self.Energy_plot(w,R,v,o,y,t,Egraph)            
