from django.db import models


# Create your models here.
def format_time(time):
    if time < 1000:
        time = f'{str(time)[:1]}:{str(time)[1:]} AM'
    elif 1000 <= time < 1200:
        time = f'{str(time)[:2]}:{str(time)[2:]} AM'
    elif 1200 <= time < 2359:
        time = f'{str(time)[:2]}:{str(time)[2:]} PM'

    return time


class Timeslot(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.SmallIntegerField()
    end_time = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{format_time(self.start_time)} - {format_time(self.end_time)}'

    class Meta:
        ordering = ['start_time']
        verbose_name_plural = 'Timeslots'
        unique_together = (('start_time', 'end_time'),)

    @property
    def title(self):
        """Returns time duration"""
        return f'{self.start_time} - {self.end_time}'


