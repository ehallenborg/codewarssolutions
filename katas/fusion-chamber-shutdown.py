# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
import math

def burner(c,h,o):
    water = math.floor(min(h/2,o));
    o = o - water
    h = h - water * 2
    co2 = math.floor(min(c,o/2))
    methane = math.floor(min(c,h/4))
    
    return water,co2,methane