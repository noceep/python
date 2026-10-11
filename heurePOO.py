
import doctest


class Heure:
    """
    Représente une heure.

    >>> h = Heure(12, 30, 45)
    >>> print(h)
    12:30:45
    """

    def __init__(self, h: int, m: int, s: int):
        """Initialise une heure.

        >>> h = Heure(12, 30, 45)
        >>> str(h)
        '12:30:45'
        """
        assert 0 <= h <= 23
        assert 0 <= m <= 59
        assert 0 <= s <= 59

        self.heure = h
        self.minute = m
        self.seconde = s

    def __str__(self) -> str:
        """Renvoie l'heure au format HH:MM:SS.

        >>> h = Heure(12, 30, 45)
        >>> str(h)
        '12:30:45'
        >>> repr(h)
        '12:30:45'
        """
        return f"{self.heure:02d}:{self.minute:02d}:{self.seconde:02d}"

    def __repr__(self) -> str:
        """Renvoie l'heure au format HH:MM:SS."""
        return str(self)

    # Accesseurs

    def get_heure(self) -> int:
        """Renvoie l'heure.

        >>> h = Heure(12, 30, 45)
        >>> h.get_heure()
        12
        """
        return self.heure

    def get_minute(self) -> int:
        """Renvoie les minutes.

        >>> h = Heure(12, 30, 45)
        >>> h.get_minute()
        30
        """
        return self.minute

    def get_seconde(self) -> int:
        """Renvoie les secondes.

        >>> h = Heure(12, 30, 45)
        >>> h.get_seconde()
        45
        """
        return self.seconde

    # Mutateurs

    def set_heure(self, h: int):
        """Modifie l'heure.

        >>> h = Heure(12, 30, 45)
        >>> h.set_heure(15)
        >>> str(h)
        '15:30:45'
        """
        assert 0 <= h <= 23
        self.heure = h

    def set_minute(self, m: int):
        """Modifie les minutes.

        >>> h = Heure(12, 30, 45)
        >>> h.set_minute(20)
        >>> str(h)
        '12:20:45'
        """
        assert 0 <= m <= 59
        self.minute = m

    def set_seconde(self, s: int):
        """Modifie les secondes.

        >>> h = Heure(12, 30, 45)
        >>> h.set_seconde(10)
        >>> str(h)
        '12:30:10'
        """
        assert 0 <= s <= 59
        self.seconde = s

    # Ajout d'heures

    def ajouter_Heure(self, h: int):
        """
        Ajoute des heures.

        >>> h = Heure(23, 0, 0)
        >>> h.ajouter_Heure(2)
        >>> print(h)
        01:00:00
        >>> h = Heure(15, 20, 10)
        >>> h.ajouter_Heure(10)
        >>> print(h)
        01:20:10
        """
        self.heure = (self.heure + h) % 24

    # Ajout de minutes

    def ajouter_Minute(self, m: int):
        """Ajoute des minutes et reporte les heures.

        >>> h = Heure(12, 59, 0)
        >>> h.ajouter_Minute(2)
        >>> print(h)
        13:01:00
        """
        self.minute += m

        if self.minute > 59:
            h = self.minute // 60
            self.minute = self.minute % 60
            self.ajouter_Heure(h)

    # Ajout de secondes

    def ajouter_Seconde(self, s: int):
        """Ajoute des secondes et reporte les minutes.

        >>> h = Heure(23, 59, 55)
        >>> h.ajouter_Seconde(10)
        >>> print(h)
        00:00:05
        """
        self.seconde += s

        if self.seconde > 59:
            m = self.seconde // 60
            self.seconde = self.seconde % 60
            self.ajouter_Minute(m)


"""
Doctest supplémentaires.

>>> h = Heure(12, 30, 45)
>>> str(h)
'12:30:45'
>>> repr(h)
'12:30:45'
>>> h.set_heure(15)
>>> h.set_minute(20)
>>> h.set_seconde(10)
>>> str(h)
'15:20:10'
>>> h.ajouter_Heure(10)
>>> str(h)
'01:20:10'
>>> h = Heure(12, 59, 0)
>>> h.ajouter_Minute(2)
>>> str(h)
'13:01:00'
>>> h = Heure(23, 59, 55)
>>> h.ajouter_Seconde(10)
>>> str(h)
'00:00:05'
"""


if __name__ == "__main__":
    doctest.testmod(verbose=True)



