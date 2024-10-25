def Re_Lp(V_c,L_p,viscosity_o):
    Re=V_c*L_p/viscosity_o
    return Re

    #Re_Lp:Air-side Reynolds number based on louver pitch
    #V_c:Maximum air velocity
    #L_p:Louver pitch
    #viscosity_o:Viscosity of air

    #in exp:Re_Lp 100~600

def colburn_j_factor(L_alpha,L_p,F_p,H,F_d,L_l,T_p,delta_f):
    j=Re_Lp()**-0.487*(L_alpha/90)**0.257*(F_p/L_p)**-0.13*(H/L_p)**-0.29*(F_d/L_p)**-0.235*(L_l/L_p)**0.68*(T_p/L_p)**-0.279*(delta_f/L_p)**-0.05
    return j

    #L_alpha:Louver angle
    #L_p:Louver pitch
    #F_p:Fin pitch
    #H:Fin height
    #F_d:Flow depth
    #L_l:Louver length
    #T_p:tube pitch
    #delta_f:Fin thickness

def fanning_friction_factor(L_alpha,L_p,F_p,H,F_d,L_l):
    f=Re_Lp**-0.781*(L_alpha/90)**0.444*(F_p/L_p)**-1.682*(H/L_p)**-1.22*(F_d/L_p)**-0.818*(L_l/L_p)**1.97
    return f

    #L_alpha:Louver angle
    #L_p:Louver pitch
    #F_p:Fin pitch
    #H:Fin height
    #F_d:Flow depth
    #L_l:Louver length

def Nusselt_number(Pr_o):
    Nu=colburn_j_factor()*Re_Lp()*Pr_o**(1/3)
    return Nu

    #Pr_o:Prandtl number of air

def pressure_drop(A_o,A_c,density_m,V_c):
    delta_P=fanning_friction_factor()*A_o/A_c*density_m*V_c**2/2
    return delta_P

    #A_o:actually be A. A:one side of the total surface area of heat exchanger A_o:Total air-side surface area
    #A_c:Minimum free-flow area for air side
    #density_m:Mean average air density
    #V_c:Maximum air velocity 

def h_o(density_m,V_c,Cp_o,Pr_o):

    h=colburn_j_factor()*density_m*V_c*Cp_o/Pr_o**(2/3)
    return h

    #h_o:Heat transfer coefficient
    #density_m:Mean average air density
    #V_c:Maximum air velocity
    #Cp_o:Specific heat of air
    #Pr_o:Prandtl number of air

'''
def coefficient_m(k_f,delta_f,F_d):
    m=((2*h_o)/k_f/delta_f*(1+delta_f/F_d))**0.5
    return m

    #h_o:Heat transfer coefficient
    #k_f:Thermal conductivity of fin
    #delta_f:Fin thickness
    #F_d:Flow depth

def fin_length(H,delta_f):
    l=H/2+delta_f
    return l

    #H:Fin height
    #delta_f:Fin thickness

def eta_f():
    eta_f=np.tanh(coefficient_m()*fin_length())/coefficient_m()/fin_length()
    return eta_f

    #eta_f:Fin efficiency

def eta_o(A_f,A_o):
    eta_o=1-A_f/A_o*(1-eta_f())
    return eta_o
    #eta_o:Surface effectiveness
    #A_f:Fin surface area
    #A_o:Total air-side surface area

def U_o(A_o,h_i,A_i,delta_w,k_w,A_w):
    term1=1/eta_o()/h_o()/A_o
    term2=1/h_i/A_i
    term3=delta_w/k_w/A_w
    U_o=1/(term1+term2+term3)/
    return U_o

    #A_o:Total air-side surface area
    #h_i:Heat transfer coefficient of water side
    #A_i:Total water-side surface area
    #delta_w:Tube wall thickness
    #k_w:Thermal conductivity of wall
    #A_w:Tube wall area
'''

def heat_transfer(A_o,T_o2,T_o1):
    Q=h_o()*A_o*(T_o2-T_o1)
    return Q

    #A_o:Total air-side surface area
    #T_o2:airside oulet temperature
    #T_o1:airside inlet temperature




