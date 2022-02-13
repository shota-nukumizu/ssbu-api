from django.db import models

WEIGHT_CHOICES = (
    ('super-heavy', 'super-heavy'),
    ('heavy', 'heavy'),
    ('heavy-middle', 'heavy-middle'),
    ('middle', 'middle'),
    ('middle-light', 'middle-light'),
    ('light', 'light'),
    ('super-light', 'super-light')
)

SERIES_CHOICES = (
    ('64', '64'),
    ('DX', 'melee'),
    ('X', 'brawl'),
    ('For', 'for'),
    ('SP', 'ultimate')
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
