def Re_Lp():
    Re=V_c*L_p/viscosity_o
    return Re

    #Re_Lp:Air-side Reynolds number based on louver pitch
    #V_c:Maximum air velocity
    #L_p:Louver pitch
    #viscosity_o:Viscosity of air

    #in exp:Re_Lp 100~600

def colburn_j_factor():
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

def fanning_friction_factor():
    f=Re_Lp**-0.781*(L_alpha/90)**0.444*(F_p/L_p)**-1.682*(H/L_p)**-1.22*(F_d/L_p)**-0.818*(L_l/L_p)**1.97
    return f

    #L_alpha:Louver angle
    #L_p:Louver pitch
    #F_p:Fin pitch
    #H:Fin height
    #F_d:Flow depth
    #L_l:Louver length

def Nusselt_number():
    Nu=colburn_j_factor()*Re_Lp()*Pr_o**(1/3)
    return Nu

    #Pr_o:Prandtl number of air

def pressure_drop():
    delta_P=fanning_friction_factor()*A_o/A_c*density_m*V_c**2/2
    return delta_P

    #A_o:actually be A. A:one side of the total surface area of heat exchanger A_o:Total air-side surface area
    #A_c:Minimum free-flow area for air side
    #density_m:Mean average air density
    #V_c:Maximum air velocity 

def h_o():

    h=colburn_j_factor()*density_m*V_c*Cp_o/Pr_o**(2/3)
    return h

    #h_o:Heat transfer coefficient
    #density_m:Mean average air density
    #V_c:Maximum air velocity
    #Cp_o:Specific heat of air
    #Pr_o:Prandtl number of air

def heat_transfer():
    Q=h_o()*A_o*(T_o2-T_o1)
    return Q

    #A_o:Total air-side surface area
    #T_o2:airside oulet temperature
    #T_o1:airside inlet temperature

def set_value():
    global V_c, L_p, viscosity_o, L_alpha, F_p, H, F_d, L_l, T_p, delta_f, Pr_o, A_o, A_c, density_m, Cp_o, T_o2, T_o1
    V_c=1               #V_c:Maximum air velocity
    L_p=1               #L_p:Louver pitch
    viscosity_o=1       #viscosity_o:Viscosity of air
    L_alpha=1           #L_alpha:Louver angle
    F_p=1               #F_p:Fin pitch
    H=1                 #H:Fin height
    F_d=1               #F_d:Flow depth
    L_l=1               #L_l:Louver length
    T_p=1               #T_p:tube pitch
    delta_f=1           #delta_f:Fin thickness
    Pr_o=1              #Pr_o:Prandtl number of air
    A_o=1               #A_o:actually be A. A:one side of the total surface area of heat exchanger A_o:Total air-side surface area
    A_c=1               #A_c:Minimum free-flow area for air side
    density_m=1         #density_m:Mean average air density
    Cp_o=1              #Cp_o:Specific heat of air
    T_o2=1              #T_o2:airside oulet temperature
    T_o1=1              #T_o1:airside inlet temperature
    return V_c,L_p,viscosity_o,L_alpha,F_p,H,F_d,L_l,T_p,delta_f,Pr_o,A_o,density_m,Cp_o,T_o2,T_o1

if __name__ == '__main__':
    set_value()
    Re_Lp()
    colburn_j_factor()
    fanning_friction_factor()
    Nusselt_number()
    pressure_drop()
    h_o()
    heat_transfer()

