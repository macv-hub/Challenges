# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Calculates the Bending Moment capacity MRd of a section

#Geometry
b = 1970 #mm
h = 600 #mm
c = 50 #mm
phi = 50 #mm
dst = h-c-phi/2
dsc = c+phi/2

#Material properties
fyk = 500 #MPa
fck = 40 #Mpa

#Reinforcement
Asc = 9820
Ast = 9820


# %%
#Concrete
gamma_c = 1.5
fcd = 0.85*fck/gamma_c #MPa
eps_cc = 0.0020
eps_cu = 0.0035

#Steel
gamma_s = 1.15
fyd = fyk/gamma_s
Es = 200000 #MPa
eps_su = 0.01
eps_y = fyd/Es


# %%
#These functions take an epsilon value as input and return a stress. To call a function use rel_c(strain value)

def rel_c(eps):
    #Stress-strain curve for concrete
    eps = abs(eps)
    if  eps <= eps_cc:
        sig = fcd*(2-eps/eps_cc)*eps/eps_cc
    elif eps > eps_cc and eps <= eps_cu:
        sig = fcd
    else:
        print("Invalid eps value")

    return(sig)

def rel_s(eps):
    #Stress-strain curve for steel
    eps = abs(eps)
    if eps <=eps_y:
        sig = eps*Es
    elif eps > eps_y and eps <= eps_su:
        sig = fyd
    else:
        print("Invalid eps value")

    return(sig)


# %%
#Bending Moment capacity calculation

x_min = dst/((eps_su/eps_cu)+1)
x_max = dst/((eps_y/eps_cu)+1)
x1 = 0
x2 = x_max
while True:     #while True means the loop will go indefinitely until a condition breaks it
    #Strains and stresses

    x = (x1+x2)/2   #Bisection method to find the NA. Since the increment method wasn't very effective, we use this! :)

    if x <= x_min: #The strain plane pivots around the bottom steel ultimate strain until the top concrete reaches its ultimate strain, then the top concrete pivots the strain plane until the bottom steel yields (balanced condition)
        eps_c = (eps_su/(dst-x))*x  
    else:
        eps_c = eps_cu
    eps_sc = (eps_c/x)*(x-dsc)
    eps_st = (eps_c/x)*(dst-x)
    eps_st = round(eps_st,5)
    sig_c = rel_c(eps_c)
    sig_sc = rel_s(eps_sc)
    sig_st = rel_s(eps_st)

    #Forces
    Fcc = b*0.8*x*sig_c
    Fsc = Asc*sig_sc
    if x < dsc:         
        Fsc = -Fsc       #Flips the force direction of the top steel depending where the NA is
    Fst = Ast*sig_st

    #Summation of forces in x -->remember: we need to check the signs are correct. More general solutions available but this is ok for now
    Fxx = Fcc+Fsc-Fst

    #Moment about tension steel
    MRd = Fcc*(dst-x/2)+Fsc*(dst-dsc)

    if Fxx > 0.01:
        x2 = x
    elif Fxx < -0.01:
        x1 = x
    else: 
        break           #if the condition is satisfied then the loop breaks
    


# %%
print("x={} mm\nFxx={} N\nMRd={} KNm".format(round(x,3),round(Fxx,3),round(MRd/1000000,3)))


# %%
#If you find a bug let me know


