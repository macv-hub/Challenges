import math
import numpy as np
import matplotlib.pyplot as plt

def area_steel(n_bars, bar_size):
    '''Takes the number of bars and bar size as integer, returns the area as float'''

    return n_bars*math.pi*(bar_size/2)**2


class force:
    def __init__(self, force):
        '''
        Takes a dictionary of the form:

        properties = {
            'omega': in KN/m,
            'Point_load': in KN
            }

        Creates a force instance
        '''

        for key in force:
            setattr(self, key, force[key])       

class beam:

    def __init__(self,properties):
        '''Takes a dictionary of the form:

        properties = {
            'name': None, #name of the beam
            'b': None, #width in mm
            'h': None, #depth in mm,
            'phi': None, #bar size in mm,
            'Ast': None, #function area_steel(n_bars, bar_diametre),
            'Asc': None, #function area_steel(n_bars, bar_diametre),
            'fck': None, #grade in MPa,
            'fyk': None, #grade in MPa,
            'c': None, #cover in mm,
            'span': None, #span in m
            }

        '''
        for key in properties:
            setattr(self, key, properties[key])

    def internal_forces(self,F):
        n_steps = 41
        F = force(F)
        x = np.linspace(0,self.span,n_steps)
        M = np.zeros(n_steps)
        V = np.zeros(n_steps)
        for i in range(0, int(n_steps/2)):
            M[i] = F.omega*self.span/2*x[i]+F.Point_load*x[i]/2-F.omega*(x[i]**2)/2
            V[i] = F.omega*self.span/2+F.Point_load/2-F.omega*x[i]
        for i in range(int(n_steps/2),n_steps):
            M[i] = F.omega*self.span/2*x[i]+F.Point_load*x[i]/2-F.omega*(x[i]**2)/2-F.Point_load*(x[i]-self.span/2)
            V[i] = F.omega*self.span/2-F.Point_load/2-F.omega*x[i]
        
        plt.title(f'Internal forces({self.name})')
        plt.plot(x, M, label = 'BMD')
        plt.plot(x, V, label = 'SFD')
        plt.legend()
        plt.plot(x,np.zeros(n_steps))
        plt.fill_between(x, 0, V,facecolor='orange')
        
        plt.show()
        
    def __str__(self):
        return str(self.name)


# properties = {
#     'name':'Beam 1',
#     'b': 1000,
#     'h': 300,
#     'phi': 25,
#     'Ast': area_steel(7,25),
#     'Asc': area_steel(7,25),
#     'fck': 40,
#     'fyk': 500,
#     'c': 60,
#     'span': 10
#     }

# F = {
#     'omega': 10,
#     'Point_load': 50
#     }


# b1 = beam(properties)
# b1.internal_forces(F)
# #help(beam)
