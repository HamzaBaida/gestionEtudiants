from django.db import models

class Etudiant(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    MENTION_CHOICES = [
        ('TB', 'Très Bien'),
        ('B', 'Bien'),
        ('AB', 'Assez Bien'),
        ('P', 'Passable'),
        ('I', 'Insuffisant'),
    ]

    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    cin = models.CharField(max_length=20)
    cne = models.CharField(max_length=20, unique=True)
    adresse = models.CharField(max_length=200)
    note_1ere = models.FloatField()
    note_2eme = models.FloatField()
    mention = models.CharField(max_length=2, choices=MENTION_CHOICES, blank=True)

    def save(self, *args, **kwargs):
        moyenne = (self.note_1ere + self.note_2eme) / 2

        if moyenne >= 85:
            self.mention = 'TB'
        elif moyenne >= 75:
            self.mention = 'B'
        elif moyenne >= 65:
            self.mention = 'AB'
        elif moyenne >= 50:
            self.mention = 'P'
        else:
            self.mention = 'I'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} ({self.cne})"
