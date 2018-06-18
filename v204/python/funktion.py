# übergeben werden
# t1 und t2

o = 0
max = t1[o]
min1 = []
mint1 = []
max1 = []
maxt1 = []
while o < len(t1)-1:
    o += 1
    if t1[o] >= max:
        print(o, t1[o], max)
        while t1[o] >= max and o < len(t1)-1:
            max = t1[o]
            o += 1
            print(o, t1[o], max)
    print(o, max)
    max1.append(max)
    maxt1.append(2*o-2)
    min = t1[o]
    o += 1
    if t1[o] <= min:
        print(o, t1[o], min)
        while t1[o] <= min and o < len(t1)-1:
            min = t1[o]
            o += 1
            print(o, t1[o], min)
    min1.append(min)
    mint1.append(2*o-2)
    max = t1[o]
o = 0
max = t2[o]
min2 = []
mint2 = []
max2 = []
maxt2 = []
while o < len(t2)-1:
    o += 1
    if t2[o] >= max:
        while t2[o] >= max and o < len(t2)-1:
            max = t2[o]
            o += 1
    messingmax2.append(max)
    messingmaxt2.append(2*o-2)
    min = t2[o]
    o += 1
    if t2[o] <= min:
        while t2[o] <= min and o < len(t2)-1:
            min = t2[o]
            o += 1
    messingmin2.append(min)
    messingmint2.append(2*o-2)
    max = t2[o]
meampl1 = []
i = 1
while i < len(messingmax1)-1:
    meampl1.append(messingmax1[i]-messingmin1[i])
    meampl1.append(messingmax1[i+1]-messingmin1[i])
    i += 1
messingamplitude1 = []
messingamplitude1.append(0)
i = 0
while i < len(meampl1):
    messingamplitude1.append((meampl1[i] + meampl1[i+1])/4)
    i += 2
messingamplitude1.append(0)
meampl2 = []
i = 0
while i < len(messingmax2)-1:
    meampl2.append(messingmax2[i]-messingmin2[i])
    meampl2.append(messingmax2[i+1]-messingmin2[i])
    i += 1
messingamplitude2 = []
i = 0
while i < len(meampl2):
    messingamplitude2.append((meampl2[i] + meampl2[i+1])/4)
    i += 2
messingamplitude2.append(0)
if len(messingmax1) > len(messingmax2):
    while len(messingmax1) > len(messingmax2):
        messingmin2.append(0)
        messingmint2.append(0)
        messingmax2.append(0)
        messingmaxt2.append(0)
        messingamplitude2.append(0)
else:
    while len(messingmax1) < len(messingmax2):
        messingmin1.append(0)
        messingmint1.append(0)
        messingmax1.append(0)
        messingmaxt1.append(0)
        messingamplitude1.append(0)
print(np.column_stack([messingamplitude1, messingamplitude2]))
kappa = []
phi = []
i = 0
while i < len(messingmax1):
    phi.append(2*np.pi*(messingmaxt2[i]-messingmaxt1[i])/80)
    if messingamplitude1[i] == 0 or messingamplitude2[i] == 0 or messingamplitude1[i] == messingamplitude2[i]:
        kappa.append(0)
    else:
        kappa.append((8520*385*0.03**2)/(2*(messingmint2[i]-messingmint1[i])*np.log(messingamplitude2[i]/messingamplitude1[i])))
    i += 1
print(kappa)
kappa1 = []
i = 0
while i < len(kappa):
    if kappa[i] <= 0:
        i += 1
    else:
        kappa1.append(kappa[i])
        i += 1
phi1 = []
i = 0
while i < len(phi):
    if phi[i] <= 0:
        i += 1
    else:
        phi1.append(phi[i])
        i += 1
