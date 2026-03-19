#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. 
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. 
# Kuljettua matkaa ei tarvitse vielä päivittää.

# luo luokan auto
class Auto:
    # määritää luodulle autolle tämän tunnuksen, nopeuden, matkan , ja nykyisen nopeuden
    def __init__(self, tunnus, nopeus):
        self.tunnus = tunnus
        self.nopeus = nopeus
        self.nopeus_nyt = 0

# laskee kiihdytykset
    def kiihdyta(self, kiihdytys):
        # tekee kiihtyvyyden laskun ja varmistaa ettei mene alle 0
        self.nopeus_nyt = max(0, min(self.nopeus, self.nopeus_nyt+kiihdytys))
        # printaa lisätävän kiihtyvyyden sekä nopeuden
        print(f"kiihdytys {kiihdytys:}  nopeus: {self.nopeus_nyt} ")

# Antaa auto luokalle annetun tunnuksen sekä nopeuden
auto = Auto("ABC-123", 142 )
# printaa auton nopeuden eri kiihdytys vaiheissa
print("kiihdykset")
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"nopeus koko kiihtyvyyden jälkeen: {auto.nopeus_nyt}\n")

# printaa auton nopeuden jarrutuksen jälkeen
print("jarrutus")
auto.kiihdyta(-200)
print(f"Nopeus jarrutuksen jälkeen: {auto.nopeus_nyt} ")
