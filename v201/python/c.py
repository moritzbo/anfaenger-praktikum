import numpy as np
from scipy.stats import sem

#  Kaloriemeterdaten Christian
cw1 = 4.182  # wärmekapa. von wasser/ in kJ/kg*Kelvin
mh1 = 0.48276  # in kg # masse heißes Wasser
mc1 = 0.23654  # in kg # masse kaltes wasser
Th1 = 363.15  # in Kelvin # Temp. heißes wasser
Tm1 = 324.25  # in Kelvin # Mischtemp. im Kalorimeter
Tc1 = 293.45  # in Kelvin # Temp. kaltes wasser
CKal1 = (cw1*mh1*(Th1-Tm1)-cw1*mc1*(Tm1-Tc1))/(Tm1-Tc1)  # CK für c kalorimeter
print("cgmg von kalori 1:", CKal1, "kJ/kg*K")
print("wärmekap von kalori 1:", CKal1/mc1)
#  Kalorimeterdaten Nils
cw2 = 4.182  # wärmekapa. von wasser/ in kJ/kg*Kelvin
mh2 = 0.75748-0.23279  # in kg # masse heißes Wasser
mc2 = 0.48262-0.23279  # in kg # masse kaltes wasser
Th2 = 356.65  # in Kelvin # Temp. heißes wasser
Tm2 = 321.55  # in Kelvin # Mischtemp. im Kalorimeter
Tc2 = 293.65  # in Kelvin # Temp. kaltes wasser
CKal2 = (cw2*mh2*(Th2-Tm2)-cw2*mc2*(Tm2-Tc2))/(Tm2-Tc2)
print("cgmg von kalori 2:", CKal2, "kJ/kg*K")
print("wärmekap von kalori 2:", CKal2/mc2)
#  Anfang Blei
# 1
cw3 = 4.182
mw3 = 0.66338  # wasser im Kaloriemeter (Mges - mglas) in kg
mk3 = 0.67968-0.13736  # mkörper in kg
Tm3 = 296.65  # Mischtemp. in Kelvin
Tw3 = 295.75  # kalte temp
Tk3 = 358.15  # heiße temp

CPb1 = ((((cw3*mw3)+CKal1)*(Tm3-Tw3))/(mk3*(Tk3-Tm3)))/mw3
print("waermekapa. von Blei Messung1 =", CPb1)
# 2
cw4 = 4.182
mw4 = 0.66338  # wasser im Kaloriemeter (Mges - mglas) in kg
mk4 = 0.67968-0.13736  # mkörper in kg
Tm4 = 295.35  # Mischtemp. in Kelvin
Tw4 = 294.65  # kalte temp
Tk4 = 356.15  # heiße temp

CPb2 = ((((cw4*mw4)+CKal1)*(Tm4-Tw4))/(mk4*(Tk4-Tm4)))/mw4
print("waermekapa. von Blei Messung2 =", CPb2)

# 3
cw5 = 4.182
mw5 = 0.90138-0.23419  # wasser im Kaloriemeter (Mges - mglas) in kg
mk5 = 0.67968-0.13736  # mkörper in kg
Tm5 = 296.55  # Mischtemp. in Kelvin
Tw5 = 294.85  # kalte temp
Tk5 = 354.15  # heiße temp

CPb3 = ((((cw5*mw5)+CKal1)*(Tm5-Tw5))/(mk5*(Tk5-Tm5)))/mw5
print("waermekapa. von Blei Messung3 =", CPb3)
Pb_mean = (CPb1+CPb2+CPb3)/3
# Pb_dif = ((Pb_mean-0.129) /0.129) * 100
print('Mittelwert Blei', Pb_mean)
# print('Prozentualer Fehler des Mittelwerts:', Pb_dif)
#  Ende Blei
#  ---------------------
#  Anfang Kupfer
#  1
cw6 = 4.182  # wärmekapa. von wasser
mw6 = 0.60404  # wasser im Kaloriemeter (Mges - mglas) in kg
mk6 = 0.37519-0.13756  # mkörper in kg
Tm6 = 313.55  # Mischtemp. in Kelvin
Tw6 = 313.05  # kalte temp
Tk6 = 353.25  # heiße temp

CCu1 = ((((cw6*mw6)+CKal2)*(Tm6-Tw6))/(mk6*(Tk6-Tm6)))/mw6
print("waermekapa. von Kupfer Messung1 =", CCu1)
#  2
cw7 = 4.182  # wärmekapa. von wasser
mw7 = 0.65272  # wasser im Kaloriemeter (Mges - mglas) in kg
mk7 = 0.37519-0.13756  # mkörper in kg
Tm7 = 296.45  # Mischtemp. in Kelvin
Tw7 = 294.55  # kalte temp
Tk7 = 354.15  # heiße temp

CCu2 = ((((cw7*mw7)+CKal1)*(Tm7-Tw7))/(mk7*(Tk7-Tm7)))/mw7
print("waermekapa. von Kupfer Messung2 =", CCu2)

#  3
cw8 = 4.182  # wärmekapa. von wasser
mw8 = 0.65272  # wasser im Kaloriemeter (Mges - mglas) in kg
mk8 = 0.37519-0.13756  # mkörper in kg
Tm8 = 298.95  # Mischtemp. in Kelvin
Tw8 = 295.35  # kalte temp
Tk8 = 358.15  # heiße temp

CCu3 = ((((cw8*mw8)+CKal1)*(Tm8-Tw8))/(mk8*(Tk8-Tm8)))/mw8
print("waermekapa. von Kupfer Messung3 =", CCu3)
Cu_mean = (CCu3+CCu2+CCu1)/3
# Cu_dif = ((Cu_mean-0.381)/0.381)*100
print('mittelwert Kupfer:', Cu_mean)
# print("prozent fehler Kupfer:", Cu_dif)
#  Ende Kupfer
#  ----------------
#  Anfang Graphit
#  1
cw9 = 4.182  # wärmekapa. von wasser
mw9 = 0.65636  # wasser im Kaloriemeter (Mges - mglas) in kg
mk9 = 0.24274-0.13753  # mkörper in kg
Tm9 = 296.15  # Mischtemp. in Kelvin
Tw9 = 295.75  # kalte temp
Tk9 = 353.45  # heiße temp

Cgraph1 = ((((cw9*mw9)+CKal2)*(Tm9-Tw9))/(mk9*(Tk9-Tm9)))/mw9
print("waermekapa. von Graphit Messung1 =", Cgraph1)

#  2
cw0 = 4.182  # wärmekapa. von wasser
mw0 = 0.59754  # wasser im Kaloriemeter (Mges - mglas) in kg
mk0 = 0.24274-0.13753  # mkörper in kg
Tm0 = 294.65  # Mischtemp. in Kelvin
Tw0 = 294.15  # kalte temp
Tk0 = 354.65  # heiße temp

Cgraph2 = ((((cw0*mw0)+CKal2)*(Tm0-Tw0))/(mk0*(Tk0-Tm0)))/mw0
print("waermekapa. von Graphit Messung2 =", Cgraph2)

#  3
cw_1 = 4.182  # wärmekapa. von wasser
mw_1 = 0.59754  # wasser im Kaloriemeter (Mges - mglas) in kg
mk_1 = 0.24274-0.13753  # mkörper in kg
Tm_1 = 298.95  # Mischtemp. in Kelvin
Tw_1 = 294.15  # kalte temp
Tk_1 = 356.55  # heiße temp

Cgraph3 = ((((cw_1*mw_1)+CKal2)*(Tm_1-Tw_1))/(mk_1*(Tk_1-Tm_1)))/mw_1
print("waermekapa. von Graphit Messung3 =", Cgraph3)
gr_mean = (Cgraph1+Cgraph2+Cgraph3)/3
print('mittelwert graphit:', gr_mean)
#  Ende Graphit
#  -----------------
m = np.array([1, 2, 3])
ckal = np.array([CKal1, CKal2, 0])
cPb = np.array([CPb1, CPb2, CPb3])
cCu = np.array([CCu1, CCu2, CCu3])
cgraph = np.array([Cgraph1, Cgraph2, Cgraph3])
np.savetxt("build/c.txt", np.column_stack([m, ckal, cPb, cCu, cgraph]), header="Nr ckal cPb cCu cgraph")
#------------------
x = [Cgraph1, Cgraph2, Cgraph3]
y = [CCu1, CCu2, CCu3]
z = [CPb1, CPb2, CPb3]
a = sem(x)
b = sem(y)
c = sem(z)
print("Mittelwertfehler graphit:", a)
print("Mittelwertfehler kupfer:", b)
print("Mittelwertfehler blei:", c)
#------------------
#  Molwärme
#Blei 1,2,3
a_Pb = 29e-6  # 1/K
k_Pb = 42e9  # m^2/N
t1_Pb = 296.65
M_Pb = 207.2
rho_Pb = 11.35e6
v0_Pb = (M_Pb)/(rho_Pb)
Cv1 = (Pb_mean*M_Pb)-9*a_Pb**2*k_Pb*(v0_Pb)*t1_Pb
print("molwärme Blei:", Cv1)

# kupfer 1,2,3
a_Cu = 16.8e-6
k_Cu = 136e9
t4_Cu = 313.55
M_Cu = 63.5
rho_Cu = 8.96e6
v0_Cu = (M_Cu)/(rho_Cu)
Cv4 = (Cu_mean*M_Cu)-(9*a_Cu**2*k_Cu*(v0_Cu)*t4_Cu)
print("molwärme kupfer:", Cv4)

a_gr = 8e-6
k_gr = 33e9
t7_gr = 296.15
M_gr = 12.0
rho_gr = 2.25e6
v0_gr = (M_gr)/(rho_gr)
Cv7 = (gr_mean*M_gr) - (9*a_gr**2*k_gr*(v0_gr)*t7_gr)
print("molwärme graphit:", Cv7)

sigma1 = np.sqrt((1/6)*((CPb3-0.129)+(CPb2-0.129)+(CPb1-0.129)))
print("sigma pb=", sigma1)
sigma2 = np.sqrt((1/6)*((CCu3-0.382)+(CCu2-0.382)+(CCu1-0.382)))
print("sigma cu =", sigma2)
sigma3 = np.sqrt((1/6)*((Cgraph3-0.715)+(Cgraph2-0.715)+(Cgraph1-0.715)))
print("sigma graphit =", sigma3)
