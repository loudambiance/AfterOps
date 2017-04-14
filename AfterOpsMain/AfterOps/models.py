from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=512)
    note = models.CharField(max_length=512)


class Contact(models.Model):
    CONTACT_TYPE = (
        ('wp', 'Work Phone'),
        ('hp', 'Home Phone'),
        ('mp', 'Mobile Phone'),
        ('e', 'e-mail'),
        ('p', 'pager'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="owning user",
    )
    type = models.CharField(max_length=2, choices=CONTACT_TYPE)
    contact = models.CharField(max_length=100)
    priority = models.IntegerField('Contact Order')


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Schedule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rotation_length = models.IntegerField()
    rotation_start = models.DateField()

class TeamScheduleTemplate(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rotation_length = models.IntegerField()
    rotation_start = models.DateField()

class ScheduleSubstitution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitution_length = models.IntegerField()
    substitution_start = models.DateField()