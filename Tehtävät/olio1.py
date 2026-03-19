
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
