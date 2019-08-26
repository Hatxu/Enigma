class Plugboard:
    def __init__(self,plug1,plug2):
        self.plug1 = plug1
        self.plug2 = plug2
    
    def __str__(self):
        return "PlugA: "+  self.plug1 + " y PlugB: "+ self.plug2
        
    def changeplug(self,value):
        if value==self.plug1:
            return self.plug2
        elif value==self.plug2:
            return self.plug1
        else:
            return "0"