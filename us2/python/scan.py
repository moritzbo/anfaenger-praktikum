import numpy as np

nummer, durchmesser, schieboben, schiebunten, amessoben, amessunten, bmessoben, bmessunten = np.genfromtxt('python/daten/bohrungen.txt', unpack=True)
durchmesser *= 10**(-2)
schieboben *= 10**(-2)
schiebunten *= 10**(-2)
amessoben *= 10**(-3)
amessunten *= 10**(-3)
bmessoben *= 10**(-3)
bmessunten *= 10**(-3)

tiefeschieb = 0.0805
durchmesserschieb = tiefeschieb - schiebunten - schieboben
prozdurchmesserschieb = abs(durchmesserschieb - durchmesser)/durchmesserschieb * 100

atiefemess = 0.08275
atiefedelta = abs(atiefemess - tiefeschieb)
adurchmessermess = atiefedelta + atiefemess - amessoben - amessunten
aprozdurchmessermess = abs(adurchmessermess - durchmesser)/adurchmessermess * 100

btiefemess = 0.08275
btiefedelta = abs(btiefemess - tiefeschieb)
bdurchmessermess = btiefedelta + btiefemess - bmessoben - bmessunten
bprozdurchmessermess = abs(bdurchmessermess - durchmesser)/bdurchmessermess * 100

np.savetxt('build/scan.txt',
    np.column_stack([nummer, durchmesser, schieboben, schiebunten, durchmesserschieb, prozdurchmesserschieb, amessoben, amessunten, adurchmessermess, aprozdurchmessermess, bmessoben, bmessunten, bdurchmessermess, bprozdurchmessermess]),
    header='nummer, durchmesser, schieboben, schiebunten, durchmesserschieb, prozdurchmesserschieb, amessoben, amessunten, adurchmessermess, aprozdurchmessermess, bmessoben, bmessunten, bdurchmessermess, bprozdurchmessermess')
