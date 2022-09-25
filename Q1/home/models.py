from django.db import models

class TaskManager(models.Model):
    category = choices = [('AI', 'Artificial Intelligence'), ('ML', 'Machine Learning'), ('IOT', 'Internet of Things')]
    hist = models.CharField(choices = category, max_length = 150, null = True, blank = True, default = "ML")
    description = models.CharField(max_length = 100, null = True, blank = True)
    due_on = models.DateField()

    def __str__(self):
        return self.hist + ' ' + self.description

    class Meta:
        verbose_name_plural = 'Task Manager'
