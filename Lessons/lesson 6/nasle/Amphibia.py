from Car import *
from Boat import *

class Amphibia(Car,Boat):
    pass

amb = Amphibia()
amb.ride()
amb.swim()