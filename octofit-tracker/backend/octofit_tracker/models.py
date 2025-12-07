from djongo import models


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    points = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.email} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    month = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.team} - {self.month}"