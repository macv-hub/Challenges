import simply_supported as ss

#Beam 1

properties1 = {
    'name':'beam 1',
    'b': 1000,
    'h': 300,
    'phi': 25,
    'Ast': ss.area_steel(7,25),
    'Asc': ss.area_steel(7,25),
    'fck': 40,
    'fyk': 500,
    'c': 60,
    'span': 10
    }

F1 = {
    'omega': 10,
    'Point_load': 50
    }


#Beam 2

properties2 = {
    'name':'beam 2',
    'b': 1000,
    'h': 300,
    'phi': 25,
    'Ast': ss.area_steel(7,25),
    'Asc': ss.area_steel(7,25),
    'fck': 40,
    'fyk': 500,
    'c': 60,
    'span': 10
    }

F2 = {
    'omega': 20,
    'Point_load': 50
    }


#Create beam objects

b1 = ss.beam(properties1)
b1.internal_forces(F1)


b2 = ss.beam(properties2)
b2.internal_forces(F2)
