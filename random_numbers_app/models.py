from django.db import models

class LotteryResults(models.Model):
    readonly_fields = ('id',)
    game_name = models.CharField(max_length=20)
    draw_date = models.CharField(max_length=10)
    numbers = models.CharField(max_length=30)
    special_num = models.CharField(max_length=2, blank=True)
    next_draw = models.CharField(max_length=10)
    jackpot = models.CharField(max_length=20)
    draw_time = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.game_name + ', ' + self.draw_date
    
    class Meta:
        ordering = ('game_name',)
