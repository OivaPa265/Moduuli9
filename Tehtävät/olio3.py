#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

# luo luokan auto
class Auto:
    # määritää luodulle autolle tämän tunnuksen, nopeuden, matkan , nykyisne nopeuden, ajan sekä matkaan meneen pituuden
    def __init__(self, tunnus, nopeus):
        self.tunnus = tunnus
        self.nopeus = nopeus
        self.nopeus_nyt = 0
        self.kulje_matka =0

# laskee kiihdytykset
    def kiihdyta(self, kiihdytys):
        # tekee kiihtyvyyden laskun ja varmistaa ettei mene alle 0
        self.nopeus_nyt = max(0, min(self.nopeus, self.nopeus_nyt+kiihdytys))

        # printaa lisätävän kiihtyvyyde n sekä nopeuden
        print(f"kiihdytys {kiihdytys:}  nopeus: {self.nopeus_nyt} ")

# laskee matkan kuluneen ajan sekä matkan tänä aikana
    def kulje(self,tunti):
        etaisyys = self.nopeus_nyt * tunti
        self.kulje_matka += etaisyys

# Antaa auto luokalle annetun tunnuksen sekä nopeuden
auto = Auto("ABC-123", 142 )

# printaa auton kiihtyvyyden matkan ja ajan
print("matka1")
auto.kiihdyta(30)
auto.kulje(1.5)

print(f"1,5 tunnin aikana auto on kulkenut {auto.kulje_matka}Km\n")
# toinen esimerkki eri ajassa
