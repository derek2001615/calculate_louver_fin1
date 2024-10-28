class cal:
    def __init__(self, V_c, L_p, viscosity_o, L_alpha, F_p, H, F_d, L_l, T_p, delta_f, Pr_o, A_o, A_c, density_m, Cp_o, T_o2, T_o1):
        self.V_c = V_c
        self.L_p = L_p
        self.viscosity_o = viscosity_o
        self.L_alpha = L_alpha
        self.F_p = F_p
        self.H = H
        self.F_d = F_d
        self.L_l = L_l
        self.T_p = T_p
        self.delta_f = delta_f
        self.Pr_o = Pr_o
        self.A_o = A_o
        self.A_c = A_c
        self.density_m = density_m
        self.Cp_o = Cp_o
        self.T_o2 = T_o2
        self.T_o1 = T_o1

def cal_Re_Lp(V_c,L_p,viscosity_o):
    Re=V_c*L_p/viscosity_o
    return Re

    #Re_Lp:Air-side Reynolds number based on louver pitch
    #V_c:Maximum air velocity
    #L_p:Louver pitch
    #viscosity_o:Viscosity of air

    #in exp:Re_Lp 100~600

def cal_colburn_j_factor(L_alpha,L_p,F_p,H,F_d,L_l,T_p,delta_f):
    j=cal_Re_Lp(V_c,L_p,viscosity_o)**-0.487 * (L_alpha/90)**0.257 * (F_p/L_p)**-0.13 * (H/L_p)**-0.29 * (F_d/L_p)**-0.235 * (L_l/L_p)**0.68 * (T_p/L_p)**-0.279 * (delta_f/L_p)**-0.05
    return j

    #L_alpha:Louver angle
    #L_p:Louver pitch
    #F_p:Fin pitch
    #H:Fin height
    #F_d:Flow depth
    #L_l:Louver length
    #T_p:tube pitch
    #delta_f:Fin thickness

def cal_fanning_friction_factor(L_alpha,L_p,F_p,H,F_d,L_l):
    f=cal_Re_Lp(V_c,L_p,viscosity_o)**-0.781 * (L_alpha/90)**0.444 * (F_p/L_p)**-1.682 * (H/L_p)**-1.22 * (F_d/L_p)**-0.818 * (L_l/L_p)**1.97
    return f

    #L_alpha:Louver angle
    #L_p:Louver pitch
    #F_p:Fin pitch
    #H:Fin height
    #F_d:Flow depth
    #L_l:Louver length

def cal_Nusselt_number(Pr_o):
    Nu=cal_colburn_j_factor(L_alpha,L_p,F_p,H,F_d,L_l,T_p,delta_f)*cal_Re_Lp(V_c,L_p,viscosity_o)*Pr_o**(1/3)
    return Nu

    #Pr_o:Prandtl number of air

def cal_pressure_drop(A_o,A_c,density_m,V_c):
    delta_P=cal_fanning_friction_factor(L_alpha,L_p,F_p,H,F_d,L_l)*A_o/A_c*density_m*V_c**2/2
    return delta_P

    #A_o:actually be A. A:one side of the total surface area of heat exchanger A_o:Total air-side surface area
    #A_c:Minimum free-flow area for air side
    #density_m:Mean average air density
    #V_c:Maximum air velocity 

def cal_h_o(density_m,V_c,Cp_o,Pr_o):

    h=cal_colburn_j_factor(L_alpha,L_p,F_p,H,F_d,L_l,T_p,delta_f)*density_m*V_c*Cp_o/Pr_o**(2/3)
    return h

    #h_o:Heat transfer coefficient
    #density_m:Mean average air density
    #V_c:Maximum air velocity
    #Cp_o:Specific heat of air
    #Pr_o:Prandtl number of air

def cal_heat_transfer(A_o,T_o2,T_o1):
    Q=cal_h_o(density_m,V_c,Cp_o,Pr_o)*A_o*(T_o2-T_o1)
    return Q

    #A_o:Total air-side surface area
    #T_o2:airside oulet temperature
    #T_o1:airside inlet temperature

def set_value():
    V_c=3.27                         #V_c:Maximum air velocity                                                                                   unit:m/s
    L_p=0.0017                       #L_p:Louver pitch                                                                                           unit:m
    viscosity_o=1.85*10**-5          #viscosity_o:Viscosity of air                                                                               unit:kg/(m*s)
    L_alpha=25                       #L_alpha:Louver angle                                                                                       unit:°
    F_p=0.0014                       #F_p:Fin pitch                                                                                              unit:m
    H=0.00815                        #H:Fin height                                                                                               unit:m
    F_d=0.02                         #F_d:Flow depth                                                                                             unit:m
    L_l=0.0064                       #L_l:Louver length                                                                                          unit:m
    T_p=0.01015                      #T_p:tube pitch                                                                                             unit:m
    delta_f=0.0001                   #delta_f:Fin thickness                                                                                      unit:m
    Pr_o=0.71                        #Pr_o:Prandtl number of air                                                                                 unit:no unit
    A_o=0.1785                       #A_o:actually be A. A:one side of the total surface area of heat exchanger A_o:Total air-side surface area  unit:m^2           guess
    A_c=0.0084                       #A_c:Minimum free-flow area for air side                                                                    unit:m^2           guess
    density_m=1.225                  #density_m:Mean average air density                                                                         unit:kg/m^3
    Cp_o=1007                        #Cp_o:Specific heat of air                                                                                  unit:J/(kg*K)
    T_o2=30                          #T_o2:airside oulet temperature                                                                             unit:°C
    T_o1=21                          #T_o1:airside inlet temperature                                                                             unit:°C
    return V_c,L_p,viscosity_o,L_alpha,F_p,H,F_d,L_l,T_p,delta_f,Pr_o,A_o,A_c,density_m,Cp_o,T_o2,T_o1

if __name__ == '__main__':
    V_c, L_p, viscosity_o, L_alpha, F_p, H, F_d, L_l, T_p, delta_f, Pr_o, A_o, A_c, density_m, Cp_o, T_o2, T_o1 = set_value()

    cal_Re_Lp(V_c,L_p,viscosity_o)
    cal_colburn_j_factor(L_alpha,L_p,F_p,H,F_d,L_l,T_p,delta_f)
    cal_fanning_friction_factor(L_alpha,L_p,F_p,H,F_d,L_l)
    cal_Nusselt_number(Pr_o)
    cal_pressure_drop(A_o,A_c,density_m,V_c)
    cal_h_o(density_m,V_c,Cp_o,Pr_o)
    cal_heat_transfer(A_o,T_o2,T_o1)

    print(cal_Re_Lp(V_c,L_p,viscosity_o))



