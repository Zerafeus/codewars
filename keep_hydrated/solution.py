#Nathan loves cycling.

#Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

#You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.


import math

def litres(time):
    return math.floor(time * 0.5)

print(litres(2))    
print(litres(1.4))  
print(litres(12.3)) 
print(litres(0.82)) 
print(litres(11.8)) 
print(litres(1787)) 
print(litres(0))