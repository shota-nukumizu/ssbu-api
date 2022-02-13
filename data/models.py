from django.db import models

WEIGHT_CHOICES = (
    ('0', 'super-heavy'),
    ('1', 'heavy'),
    ('2', 'heavy-middle'),
    ('3', 'middle'),
    ('4', 'middle-light'),
    ('5', 'light'),
    ('6', 'super-light')
)

SERIES_CHOICES = (
    ('1', '64'),
    ('2', 'melee'),
    ('3', 'brawl'),
    ('4', 'for'),
    ('5', 'ultimate')
)

class CharacterModel(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=10, choices=SERIES_CHOICES)
    image = models.ImageField(upload_to='')
    type = models.CharField(max_length=15, choices=WEIGHT_CHOICES)
    weight = models.IntegerField()
    walk_spead = models.FloatField()
    dash_speed = models.FloatField()
    step_speed = models.FloatField()

    def __str__(self):
        return self.name
