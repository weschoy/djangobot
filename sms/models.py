from django.db import models

class Order(models.Model):
    # Model has 2 attributes. Phone and a dict called data.
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()

    def handleInput(self, sInput):
        # this is called for each turn
        # self.data["state"] starts out as WELCOMING
        aReturn = []
        sState=self.data["state"]
        if  sState== "WELCOMING":
            aReturn.append("Welcome to Rich's pizza")
            aReturn.append("Would you like a SMALL, MEDIUM, or LARGE?")
            self.data["state"] = "SIZE"
        elif sState == "SIZE":
            self.data["size"] = sInput.lower()
            aReturn.append("What toppings would you like?")
            aReturn.append("(please enter a list with commas)")
            self.data["state"] = "TOPPINGS" 
        elif sState == "TOPPINGS":
            self.data["toppings"] = sInput.lower()
            aReturn.append("Would you like drinks with that?")
            aReturn.append("(please enter a list with commas or NO)")
            self.data["state"] = "DRINKS"   
        elif sState == "DRINKS":
            if sInput.lower() != "no":
                self.data["drinks"] = sInput.lower()
            aReturn.append("Thank you for your order")
            aReturn.append(self.data["size"] + " pizza. With " + self.data["toppings"])
            try:
                aReturn.append(self.data["drinks"])
            except:
                pass
            aReturn.append("Please pickup in 20 minutes")
            self.data["state"] = "DONE"

        return aReturn

    def isDone(self):
        # this is also called for each turn
        if self.data["state"] == "DONE":
            return True
        else:
            return False
    def getState(self):
        return self.data["state"]
    def getSize(self):
        return self.data["size"]
    def getToppings(self):
        return self.data["toppings"]
    def getDrinks(self):
        try:
            return self.data["drinks"]    
        except:
            return None
    class Meta:
        # this sets up a SQL index on the phone field
        indexes = [models.Index(fields=['phone'])]
