from django.db import models

class oregon_results(models.Model):
    draw_date = models.CharField(max_length=10)
    numbers = models.CharField(max_length=20)

    def __str__(self):
        return self.draw_date + ', ' + self.numbers
    
    class Meta:
        ordering = ('draw_date',)
