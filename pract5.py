import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#1 define linguistic variables (inputs and output)
#Example: Tipping problem - quality food service and tip
quality= ctrl.Antecedent(np.arange(0,11,1),'quality')
service= ctrl.Antecedent(np.arange(0,11,1),'service')
tip= ctrl.Consequent(np.arange(0,26,1),'tip')

#2 define membership function
quality['poor']=fuzz.trimf(quality.universe,[0,0,5])
quality['average']=fuzz.trimf(quality.universe,[0,5,10])
quality['good']=fuzz.trimf(quality.universe,[5,10,10])

service['poor']=fuzz.trimf(service.universe,[0,0,5])
service['average']=fuzz.trimf(service.universe,[0,5,10])
service['good']=fuzz.trimf(service.universe,[5,10,10])

tip['low']=fuzz.trimf(tip.universe,[0,0,13])
tip['medium']=fuzz.trimf(tip.universe,[0,13,25])
tip['high']=fuzz.trimf(tip.universe,[13,25,25])

#3. define fuzzy rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low']) 
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(quality['good'] & service['good'], tip['high'])
quality.view()
quality["average"].view()
service.view()
#rule1.view()

#4.build the control system
tipping_ctrl= ctrl.ControlSystem([rule1, rule2, rule3])
tipping_simulation= ctrl.ControlSystemSimulation(tipping_ctrl)

#5. provide inputs and compute outputs
tipping_simulation.input['quality']=8.5
tipping_simulation.input['service']=8.8
tipping_simulation.compute()

#6. display result
print(f"Predicted Tip:{tipping_simulation.output['tip']:.2f}%")
tip.view(sim=tipping_simulation)