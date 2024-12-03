from fractions import Fraction

"""
Pythagorean System with 53 Intervals per Octave

This class generates a Pythagorean tuning system with 53 intervals within a single octave. 
Pythagorean tuning is based on constructing intervals through a succession of perfect fifths, 
where the ratio of a perfect fifth is 3/2.

---
Historical Background:
This system was first proposed in Europe by the Danish mathematician and astronomer 
Nicolas Mercator in the 17th century. He found it mentioned in the writings of the Chinese 
music theorist King Fang (2nd century BCE). The intervallic structure of this system, consisting 
entirely of fifths, is achieved by successively multiplying the interval 3/2 for 53 iterations 
and reducing all resulting ratios within the range of a single octave.

Although the Pythagorean system is no longer in widespread use in Western music, it is still 
employed, with variations in scale structures, in certain musical traditions such as those of 
China and the Arab world.

References:
"The Numbers of Music - Elements of Interval Calculation and Tuning Systems," Walter Branchi,
pp. 36-38.      The citation has been translated from Italian. ("I numeri della musica - 
Elementi di calcolo degli intervalli e sistemi d'intonazione")
---

Process:
1. The fundamental ratio (1/1) is used as the base.
2. At each step, a perfect fifth is "added" by multiplying the previous ratio by 3/2.
3. If the resulting ratio exceeds the octave (2/1), it is reduced by dividing by 2, bringing 
   it back within the octave range.
4. This process is repeated 53 times to generate the 53 intervals.
5. Finally, the ratios are sorted in ascending order based on their numerical value 
   (numerator/denominator).
6. Each ratio is then multiplied by a fundamental frequency to calculate the corresponding 
   real frequencies.

The class includes:
- A method to generate the ratios within the octave.
- A sorting algorithm for the ratios based on their numerical value.
- A conversion of the ratios into frequencies using a user-defined fundamental frequency.
"""


class SistemaPitagorico:
    def __init__(self, fondamentale=32, ottava=2):
        self.fondamentale = fondamentale*ottava
        self.rapporti = self.genera_rapporti()
        self.ordina_rapporti()  # Ordina i rapporti in base al loro valore reale
        self.frequenze = self.calcola_frequenze()

    def genera_rapporti(self):
        rapporti = [Fraction(1, 1)]  # La fondamentale è 1/1
        rapporto_quinta = Fraction(3, 2)  # Rapporto di quinta

        for _ in range(1, 53):  # Creiamo 53 intervalli
            prossimo_rapporto = rapporti[-1] * rapporto_quinta
            # Riduci il rapporto all'interno dell'ottava
            while prossimo_rapporto >= 2:
                prossimo_rapporto /= 2
            rapporti.append(prossimo_rapporto)
        
        return rapporti

    def calcola_frequenze(self):
        return [float(rapporto * self.fondamentale) for rapporto in self.rapporti]

    def ordina_rapporti(self):
        # Ordina i rapporti in base al valore reale
        self.rapporti.sort(key=lambda rapporto: rapporto.numerator / rapporto.denominator)

    def __repr__(self):
        return (f"SistemaPitagorico(fondamentale={self.fondamentale}, "
                f"rapporti={self.rapporti}, frequenze={self.frequenze})")

# Esempio d'uso
sistema = SistemaPitagorico()
print("Rapporti ordinati automaticamente:")
print(sistema.rapporti)
print("\nFrequenze corrispondenti:")
print(sistema.frequenze)
