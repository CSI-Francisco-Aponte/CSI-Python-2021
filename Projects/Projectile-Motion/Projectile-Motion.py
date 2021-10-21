import math
import os
from ExperimentData import ExperimentData
from pathlib import Path
import json

# Here i defined the variables
# gun = "APB"
# cartridge = "9x18mm"
# bullet = "9x18mm PM BZhT gzh"
# velocity = 325
# buildingName = "Birj Khalifa"
# buildingHeight = 828

# Here i told the program to use the variables i just defined , specifically: velocity and building height, to use math to find out the time the bullet wil travel, to then find the distance the bulllet will travel, considering there is no air resistance.
# time = math.sqrt((2*buildingHeight)/9.8)
# distance = velocity * time

# Here i made a descriptive paragrapgh describing the experiment using the variables and the results from the previous equation.
# print(f"In this experiment, we are climbing {buildingHeight} meters to the top of {buildingName} and shooting a {gun} with a cartidge of {cartridge} using a {bullet}. Considering there is no air resistance, the bullet will travel with a velocity of {velocity}m/s and a distance of {distance}meters ")

def calculateBulletDT(experimentData: ExperimentData):
    time = math.sqrt(2*experimentData.buildingHeight / experimentData.gravity)
    distance = experimentData.velocity * time

# experimentalData = {"gun" : "APB"
# "cartridge" : "9x18mm"
# "bullet" : "9x18mm PM BZhT gzh"
# "velocity" : 325
# "buildingName" : "Birj Khalifa"
# "buildingHeight" : 828}

    print(f"In this experiment, we are climbing {experimentData.buildingHeight} meters to the top of {experimentData.buildingName} and shooting a {experimentData.gun} with a cartidge of {experimentData.cartridge} using a {experimentData.bullet}. Considering there is no air resistance, the bullet will travel with a velocity of {experimentData.velocity}m/s and a distance of {distance}meters ")

# calculateBulletDT("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00)


myDataSet = [

ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, 9.8),
ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, 9.8),
ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, 9.8),
ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, 9.8),
ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, 9.8)
]

calculateBulletDT(mydata[0])

myOutputPath = Path(__file__) . parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

with open (myOutputFilePath, 'w') as outfile:
    json.dump(mydata.__dict__, outfile)