from statistics import mode
import uuid
from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="questions")
    question_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question_text

    def calculate_percentage(self):
        answers = self.answers.all()
        total_votes = 0
        for answer in answers:
            total_votes += answer.counter
        
        payload = []
        for answer in answers:
            payload.append(int((answer.counter / total_votes) * 100))

        return payload


class Answers(BaseModel):
    question = models.ForeignKey(Question , on_delete=models.CASCADE , related_name="answers")
    answer_text = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def calculate_percentage(self):
        answers = self.question.answers.all()
        total_votes = 0
        for answer in answers:
            total_votes += answer.counter
        
        payload = []
        try:
            return int((self.counter / total_votes) * 100)
        except Exception as e:
            return 0   


        #formula = C / V * 100

    def __str__(self) -> str:
        return self.answer_text