from django.db import models

# Create your models here.

class userRank(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    deposit = models.IntegerField(default=1000000)
    earning_rate = models.FloatField(default=0)
    # age = models.PositiveIntegerField(null=True)
    
    class Meta:
        # managed = False
        db_table = 'userrank'
        
    def __str__(self) -> str:
        return f"{self.username, self.deposit, self.earning_rate}"
    
    def json(self):
        return {'username':self.username, 'deposit' : self.deposit, 'earning_rate' : self.earning_rate}
    

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
        # managed = False
        db_table = 'student'

    def __str__(self) -> str:
        # return self.name
        return f"{self.name, self.grade, self.age}"
    
    def json(self):
        return {'name':self.name, 'grade' : self.grade, 'age' : self.age, 'home_address' : self.home_address, 'gender' : self.gender}



class Sessions(models.Model):
    sessionId = models.AutoField(primary_key=True)
    
    class Meta:
        # managed = False
        db_table = 'sessions'
        
    def __str__(self) -> str:
        # return self.name
        return f"{self.sessionId}"


class Ip(models.Model):
    ipId = models.AutoField(primary_key=True)
    
    class Meta:
        # managed = False
        db_table = 'ip'
        
    def __str__(self) -> str:
        # return self.name
        return f"{self.ipId}"


class Affiliation(models.Model):
    affiliationId = models.AutoField(primary_key=True)
    ip = models.ForeignKey("Ip", null=False, db_column="ipId", on_delete=models.CASCADE)
    session = models.ForeignKey("Sessions", null=False, db_column="sessionId", on_delete=models.CASCADE)
    
    class Meta:
        # managed = False
        db_table = 'affiliation'
        
    def __str__(self) -> str:
        # return self.name
        return f"{self.affiliationId, self.ip, self.session}"