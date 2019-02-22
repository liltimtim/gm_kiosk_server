from django.db import models
from django.contrib.auth import get_user_model
import random


def __create_four_digit_code__():
    """
    Creates a pseudo random 4 digit string from int between 1000 and 9999 inclusive.
    :return: string of four random digits ex: 1234
    """
    return str(int(random.uniform(1000, 9999)))


class Kiosk(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    players = models.ManyToManyField(get_user_model(), blank=True)
    join_code = models.CharField(
        max_length=4,
        null=False,
        blank=False,
        default=__create_four_digit_code__)  # Code used to attach to kiosk

    def __str__(self):
        return self.name
