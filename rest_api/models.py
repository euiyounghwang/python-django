from django.db import models

# Create your models here.

class userRank(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    deposit = models.IntegerField(default=1000000)
    earning_rate = models.FloatField(default=0)
    # age = models.PositiveIntegerField(null=True)
    
    class Meta:
        managed = False
        db_table = 'userank'
        
    def __str__(self) -> str:
        return f"{self.username, self.deposit, self.earning_rate}"
    
    def json(self):
        return {'username':str(self.username)}
    

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
                        ("Male", "M"), 
                        ("Female", "F")
                      ]
    name = models.CharField(max_length=255)
    grade = models.IntegerField()
    age = models.IntegerField()
    home_address = models.CharField(max_length=55)
    date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    # human = models.ForeignKey('userRank', on_delete = models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self) -> str:
        # return self.name
        return f"{self.name, self.grade, self.age}"
    
    def json(self):
        return {'name':str(self.name)}

