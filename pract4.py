import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#1. define linguistic variables(inputs and outputs)
temperature = ctrl.Antecedent(np.arange(15,45,1),'temperature')
humidity = ctrl.Antecedent(np.arange(1,101,1),'humidity')
fan_speed = ctrl.Consequent(np.arange(0,101,1),'fan_speed')
#2. define membership function 
# for temperature 
temperature["low"]=fuzz.trimf(temperature.universe,[15,15,25])
temperature["medium"]=fuzz.trimf(temperature.universe,[20,25,30])
temperature["high"]=fuzz.trimf(temperature.universe,[25,40,45])
#for humidity
humidity["low"]=fuzz.trimf(humidity.universe,[0,0,50])
humidity["medium"]=fuzz.trimf(humidity.universe,[25,50,75])
humidity["high"]=fuzz.trimf(humidity.universe,[50,100,100])
#for the speed of the fan
fan_speed["low"]=fuzz.trimf(fan_speed.universe,[0,0,50])
fan_speed["medium"]=fuzz.trimf(fan_speed.universe,[25,50,75])
fan_speed["high"]=fuzz.trimf(fan_speed.universe,[25,100,100])
#
rule1=ctrl.Rule(temperature['high'] & humidity["high"],fan_speed["high"])
rule2=ctrl.Rule(temperature['medium'] & humidity["high"],fan_speed["medium"])
rule3=ctrl.Rule(temperature['low'] & humidity["low"],fan_speed["low"])
#Control system
fan_ctrl= ctrl.ControlSystem([rule1,rule2,rule3])
fan_simulation= ctrl.ControlSystemSimulation(fan_ctrl)
#5 input values and perform computation
fan_simulation.input["temperature"]=30
fan_simulation.input["humidity"]=75
#perform computation
fan_simulation.compute()
fan_speed_value=fan_simulation.output["fan_speed"]
print(fan_speed_value)
#

