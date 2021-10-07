import math

# Here i defined the variables
gun = "APB"
cartridge = "9x18mm"
bullet = "9x18mm PM BZhT gzh"
velocity = 325
buildingName = "Birj Khalifa"
buildingHeight = 828

time = math.sqrt((2*buildingHeight)/9.8)
distance = velocity * time

print(f"In this experiment, we are climbing {buildingHeight} meters to the top of {buildingName} and shooting a {gun} with a cartidge of {cartridge} using a {bullet}. The bullet will travel with a velocity of {velocity}m/s and a distance of {distance}meters ")