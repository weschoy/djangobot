from django.db import models

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()
    def handleInput(self, sInput):
        aReturn = []
        sState=self.data["state"]
        if sState=="WELCOMING":
            aReturn.append("Welcome to Wesley's pizza")
            aReturn.append("Would you like a SMALL, MEDIUM, or LARGE?")
            self.data["state"]="SIZE"
        elif sState=="SIZE":
            self.data["size"]=sInput.lower()
            aReturn.append("What toppings would you like?")
            aReturn.append("Please enter a list with commas")
            self.data["state"]="TOPPINGS"
        elif sState=="TOPPINGS":
            self.data["toppings"]=sInput.lower()
            aReturn.append("Would you like drinks with that?")
            aReturn.append("Please enter a list with commas or NO")
            self.data["state"]="DRINKS"
        elif sState=="DRINKS":
            if sInput.lower() !="no":
                self.data["drinks"]=sInput.lower()
            aReturn.append("Thank you for your order")
            aReturn.append(self.data["size"]+" pizza with "+self.data["toppings"])
            try:
                aReturn.append(self.data["drinks"])
            except:
                pass
            aReturn.append("Please pick up in 20 minutes")
            self.data["state"]="DONE"
        return aReturn
    def isDone(self):
        if self.data["state"]=="DONE":
            return True
        else:
            return False