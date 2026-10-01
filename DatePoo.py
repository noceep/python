def est_bissextile(annee:int) -> bool:
    '''
    Vérifie si une année est bissextile.
    >>> est_bissextile(2024)
    True
    >>> est_bissextile(2023)
    False
    >>> est_bissextile(2000)
    True
    >>> est_bissextile(1999)
    False
    '''
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 ==  0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


JoursAcceptables = {
    1: 31,   # Janvier
    2: 28,   # Février (+1 si bissextile)
    3: 31,   # Mars
    4: 30,   # Avril
    5: 31,   # Mai
    6: 30,   # Juin
    7: 31,   # Juillet
    8: 31,   # Août
    9: 30,   # Septembre
    10: 31,  # Octobre
    11: 30,  # Novembre
    12: 31   # Décembre
}


class Date:

    def __init__(self, J:int, M:int, A:int):
        """
        this __init__, 'Innit bruv ?

        Test :
        >>> Date(29,2,2024)
        <__main__.Date object at 0x0000018DC1777390>
        """
        assert A > 0, "Année incorrecte"
        assert M in JoursAcceptables, "Mois incorrect"

        jours = JoursAcceptables.copy()

        if est_bissextile(A):
            jours[2] = 29

        assert J <= jours[M] and J > 0, "Jour incorrect"

        self.jour = J
        self.mois = M
        self.annee = A


# Voir un objet
    # print
    def __str__(self)->str:
        """
        strrrrrr..... Strike !!!

        >>> print(f)
        29:02:2024
        """
        if self.jour < 10 and self.mois < 10:
            return "0" + str(self.jour) + ":" + "0" + str(self.mois) + ":" + str(self.annee)
        elif self.jour < 10:
            return "0" + str(self.jour) + ":" + str(self.mois) + ":" + str(self.annee)
        elif self.mois < 10:
            return str(self.jour) + ":" + "0" + str(self.mois) + ":" + str(self.annee)
        return str(self.jour) + ":" + str(self.mois) + ":" + str(self.annee)


    # Dans python
    def __repr__(self)->str:
        """
        Reprise de dribble.
        """
        return self.__str__()


# Accesseurs et mutateurs
    """
    Accesseurs et mutateurs pour les attributs jour, mois et année.

    PS : C'est pas du volleyball, à ne pas confondre...
    """

    def __getjour__(self):
        return self.jour

    def __getmois__(self):
        return self.mois

    def __getannee__(self):
        return self.annee

    def __getjoursvalides__(self):
        jours = JoursAcceptables.copy()

        if est_bissextile(self.annee):
            jours[2] = 29

        return jours


    def __setjour__(self, new):
        assert 1 <= new <= self.__getjoursvalides__()[self.mois], "Jour incorrect"
        self.jour = new

    def __setmois__(self, new):
        assert new in JoursAcceptables, "Mois incorrect"
        assert self.jour <= self.__getjoursvalides__()[new], "Jour incorrect"
        self.mois = new

    def __setannee__(self, new):
        assert new > 0, "Année incorrecte"

        jours = JoursAcceptables.copy()

        if est_bissextile(new):
            jours[2] = 29

        assert self.jour <= jours[self.mois], "Jour incorrect"
        self.annee = new

# Méthodes spécifiques

    def __eq__(self, autre):
        """
        Vérifie si deux dates sont égales.

        Pourquoi les programmeurs aiment-ils la nature ?
        Parce qu'elle a beaucoup de bugs.
        """
        return (self.jour == autre.jour
                and self.mois == autre.mois
                and self.annee == autre.annee)


    def __lt__(self, autre):
        """
        Vérifie si une date est inférieure à une autre.

        Peut-être que les programmeurs aiment les araignées parce qu'elles sont de bons débogueurs.
        """
        if self.annee != autre.annee:
            return self.annee < autre.annee

        if self.mois != autre.mois:
            return self.mois < autre.mois

        return self.jour < autre.jour


    def ajouter_jours(self, nombre:int):
        """
        Ajoute ou retire un nombre de jours à la date.

        Peut-être que ces blagues sont nulles, mais elles te font oublier le fait que
        il n'y a aucun test dans mes docstrings.
        """
        if nombre > 0:
            for i in range(nombre):
                self.jour = self.jour + 1

                if self.jour > self.__getjoursvalides__()[self.mois]:
                    self.jour = 1
                    self.mois = self.mois + 1

                    if self.mois > 12:
                        self.mois = 1
                        self.annee = self.annee + 1

        elif nombre < 0:
            for i in range(-nombre):

                self.jour = self.jour - 1

                if self.jour < 1:
                    self.mois = self.mois - 1

                    if self.mois < 1:
                        self.mois = 12
                        self.annee = self.annee - 1

                    self.jour = self.__getjoursvalides__()[self.mois]


    def ecart_en_jours(self, autre):
        """
        Calcule l'écart en jours entre deux dates.

        S'en est une bonne, mais je ne sais pas si tu la comprendras. Pourquoi les programmeurs confondent-ils Halloween et Noël ?
        Parce que OCT 31 == DEC 25.
        """
        total1 = 0
        total2 = 0

        for annee in range(1, self.annee):
            if est_bissextile(annee):
                total1 = total1 + 366
            else:
                total1 = total1 + 365

        for mois in range(1, self.mois):
            total1 = total1 + self.__getjoursvalides__()[mois]

        total1 = total1 + self.jour

        for annee in range(1, autre.annee):
            if est_bissextile(annee):
                total2 = total2 + 366
            else:
                total2 = total2 + 365

        for mois in range(1, autre.mois):
            total2 = total2 + autre.__getjoursvalides__()[mois]

        total2 = total2 + autre.jour

        return abs(total2 - total1)

# Méthodes +

    def jours_annee(self):
        """
        Retourne le nombre de jours dans l'année.
        
        Pas de blague ici j'ai plus d'inspiration.
        """
        if est_bissextile(self.annee) == True:
            return 366
        return 365


    def jours_restants(self, date_fin):
        """
        Calcule le nombre de jours entre deux dates.

        Ok Claude, fait mes exercices de nsi pour moi.
        FAIT AUCUNE ERREUR.
        """
        return self.ecart_en_jours(date_fin)


    def mois_restants(self, date_fin):
        """
        Calcule le nombre de mois entre deux dates.
        
        C'est pas une blague, mais je conseille de ne pas faire ça avec des dates trop éloignées, ça sera long.
        """
        mois = (date_fin.annee - self.annee) * 12
        mois = mois + date_fin.mois - self.mois

        if date_fin.jour < self.jour:
            mois = mois - 1

        return mois


    def annees_restantes(self, date_fin):
        """
        Calcule le nombre d'années entre deux dates.
       
        
        """
        annees = date_fin.annee - self.annee

        if (date_fin.mois, date_fin.jour) < (self.mois, self.jour):
            annees = annees - 1

        return annees
