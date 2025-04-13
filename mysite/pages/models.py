from django.db import models

#Create the database structure with column names, types, and specifications
class Operation(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operator = models.CharField(max_length=1)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.operator} {self.num2} = {self.result}"