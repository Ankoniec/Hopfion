import numpy as np
from numba import jit


class Simulation:
    def __init__(self, x0:float, y0:float, z0:float,
                t:float, field_type:str , dt:float=0.05,
                dx:float=0.001, dy:float=0.001, dz:float=0.001) -> object:
  
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

        self.t = t
        self.dt = dt
        self.field_type = field_type

        self.dx = dx
        self.dy = dy
        self.dz = dz

    
    @staticmethod
    @jit(nopython=True)
    def Riemann_Silberstein_vector(x:float, y:float, z:float, t:float) -> np.ndarray:
        r2 = x**2 + y**2 + z**2
        c1 = complex(x,-z)
        c2 = complex(t+y,-1)
        Fx = c1**2 - c2**2
        Fy = 2*c1*c2
        Fz = (c1**2 + c2**2)*complex(0,1)
        C = 4/(np.pi*(-complex(t,-1)**2+r2))**3
        return np.array([Fx*C,Fy*C,Fz*C])


    @staticmethod
    @jit(nopython=True)
    def normalize(Fx:float, Fy:float, Fz:float) -> np.ndarray:
        C = np.sqrt(Fx**2+Fy**2+Fz**2)
        return np.array([Fx/C, Fy/C, Fz/C])


    def field_line(self) -> tuple:
        Lx = [self.x0]
        Ly = [self.y0]
        Lz = [self.z0]
        i=0

        while 1:
            if self.field_type=='magnetic':
                self.Fx, self.Fy, self.Fz = self.Riemann_Silberstein_vector(Lx[i],Ly[i],Lz[i],self.t).imag
            if self.field_type=='electric':
                self.Fx, self.Fy, self.Fz = self.Riemann_Silberstein_vector(Lx[i],Ly[i],Lz[i],self.t).real
                
            self.Fx, self.Fy, self.Fz = self.normalize(self.Fx, self.Fy, self.Fz)
            Lx.append(Lx[i] + self.dx*self.Fx)
            Ly.append(Ly[i] + self.dy*self.Fy)
            Lz.append(Lz[i] + self.dz*self.Fz)
            
            if (i>100 and abs(Lx[0]-Lx[-1])<0.01 
                and abs(Ly[0]-Ly[-1])<0.01 
                and abs(Lz[0]-Lz[-1])<0.01):
                break
            i+=1

        self.t += self.dt
        
        return Lx, Ly, Lz


