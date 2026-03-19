# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. 
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. 
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

# luo luokan auto
class Auto:
# määritää luodulle autolle tämän tunnuksen, nopeuden, matkan , ja nykyisen nopeuden
    def __init__(self, tunnus, nopeus):
     self.tunnus = tunnus 
     self.nopeus = nopeus
     self.nyt =0
     self. nopeus_nyt =0

# Antaa auto luokalle annetun tunnuksen sekä nopeuden
Uusi_auto =Auto("ABC-123",142 )

# printaa auton nopeuden, tunnuksen , matkan sekä nopeuden
print("auto")
print(f"tunnus {Uusi_auto.tunnus}")
print(f"nopeus {Uusi_auto.nopeus}")
print(f"nyt {Uusi_auto.nyt}")
print(f"matka {Uusi_auto.nopeus_nyt}")
