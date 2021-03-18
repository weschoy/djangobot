from django.db import models

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()
    def handleInput(self, sInput):
        aReturn = []
        aReturn.append("Message from bot isn't the opinion of the programmer")
        aReturn.append("I know you are " + sInput + " but what am I?")
        try:
            self.data['sInput'] += ", " + sInput
        except:
            self.data['sInput'] = sInput
        return aReturn