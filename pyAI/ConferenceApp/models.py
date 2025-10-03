from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Conference(models.Model):
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer Science & Artificial Intelligence"),
        ("SE","Science & Engineering"),
        ("SSE","Social Sciences & Education"),
        ("IT","Interdisciplinary Themes"),
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=50)
    description=models.TextField(validators=
                                [MaxLengthValidator(30,"vous avez dépassé la longueur maximale")]  
                                 )
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date>self.end_date:
            raise ValidationError("la date de début doit etre inferieure a la date de fin")


class Submission(models.Model):
    submission_id=models.CharField(max_length=255,primary_key=True,unique=True)
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keyword=models.TextField()
    paper=models.FileField(
        upload_to="papers/"
    )
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")

class OrganizingCommittee(models.Model):
    ROLE=[
        ("chair","chair"),
        ("co-chair","co-chair"),
        ("member","member"),
    ]
    committee_role=models.CharField(max_length=255,choices=ROLE,default="member")
    date_joined=models.DateField()
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="committees")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="committees")




