import random

STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'
ZACETEK = 'Z'

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka.upper() not in self.geslo.upper()]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka.upper() in self.geslo.upper()]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        return not self.poraz() and len(self.pravilne_crke()) == len(set(self.geslo)) 

    def pravilni_del_gesla(self):
        pravilno = ''
        for crka in self.geslo.upper():
            if crka in self.crke:
                pravilno += crka + ' '
            else:
                pravilno += '_ '
        return pravilno

        # return ''.join([c if c in self.crke else '_' for c in self.geslo.upper()])
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA 
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = f.read().split()     

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)


class Vislice:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else: 
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]   #namesto stanja pi??emo pod??rtaj, saj je to spremenljivka, ki je ne potrebujemo
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)



