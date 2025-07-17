"""
    Models for the polls application.

    Defines Question and Choice models representing
    poll questions and their possible choices.
"""

from django.db import models

class Question(models.Model):
    """
    Represents a poll question.

    :param question_text: The text of the question
    :type question_text: str
    :param pub_date: The publication date of the question
    :type pub_date: datetime
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.question_text)


class Choice(models.Model):
    """
    Represents a choice for a poll question.

    :param question: ForeignKey to the related Question
    :type question: Question
    :param choice_text: Text of the choice
    :type choice_text: str
    :param votes: Number of votes received, defaults to 0
    :type votes: int, optional
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
