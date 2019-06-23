'Class for journeyer objects'
class journeyer:
    name = ""
    depart = ""
    destination = ""
    number = ""
    
    def __init__(self, name, depart, destination, number):
        self.name = name
        self.depart = depart
        self.destination = destination
        self.number = number