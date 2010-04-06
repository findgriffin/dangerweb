from django.db import models

# Create your models here.
class Keyword(models.Model):
    score = models.IntegerField()
    word = models.CharField(max_length=40)

    def __unicode__(self):
        return self.word+u" | score:"+unicode(self.score)
        

class Character(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __unicode__(self):
        return self.firstname+self.lastname

class Quote(models.Model):
    source = models.CharField(max_length=30)
    epno = models.SmallIntegerField()
    title = models.CharField(max_length=40)
    season = models.SmallIntegerField()
    characters = models.ManyToManyField(Character)
    keywords = models.ManyToManyField(Keyword)
    popularity = models.SmallIntegerField()
    text = models.TextField()

    def __unicode__(self):
        return unicode(self.season)+u"."+unicode(self.epno)+self.text

class User(models.Model):
    ip_addr = models.IPAddressField()
    rint_1 = models.IntegerField()
    rint_2 = models.IntegerField()
    last_vote = models.DateTimeField()
    
class Vote(models.Model):
    quote = models.ForeignKey(Quote)
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    search_string = models.TextField()
