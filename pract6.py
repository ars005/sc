import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Step 1: Define Fuzzy Input & Output Variables
distance= ctrl.Antecedent(np.arange(0.1,2.3,0.01), 'distance')
angle= ctrl.Antecedent(np.arange(-90,91 , 1), 'angle')
deviation=ctrl.Consequent(np.arange(0,1.1,0.01),'deviation')# Normalized Deviation

#Step 2: Membership Functions
#Distance: Near,Medium,Far
distance['Near']=fuzz.trimf(distance.universe,[0.1,0.1,1.0])
distance['Medium']=fuzz.trimf(distance.universe,[0.5,1.2,1.9])
distance['Far']=fuzz.trimf(distance.universe,[1.2,2.2,2.2])

#Angle: Negative(left),Zero(Center),Positive(Right)
angle['Left']=fuzz.trimf(angle.universe,[-90,-45,0])
angle['Center']=fuzz.trimf(angle.universe,[-10,0,10])
angle['Right']=fuzz.trimf(angle.universe,[0,45,90])

#Deviation:Low,Medium,High
deviation['Low']=fuzz.trimf(deviation.universe,[0.0,0.0,0.4])
deviation['Medium']=fuzz.trimf(deviation.universe,[0.2,0.5,0.8])
deviation['High']=fuzz.trimf(deviation.universe,[0.6,1.0,1.0])

#Step 3:Define Fuzzy rules
rules=[
    ctrl.Rule(distance['Near'] & angle['Center'],deviation['Low']),
    ctrl.Rule(distance['Near'] &(angle['Left'] | angle['Right']),deviation['Medium']),
    ctrl.Rule(distance['Medium'] & angle['Center'],deviation['Low']),
    ctrl.Rule(distance['Medium'] &(angle['Left'] | angle['Right']),deviation['Medium']),
    ctrl.Rule(distance['Far'] & angle['Center'],deviation['Medium']),
    ctrl.Rule(distance['Far'] &(angle['Left'] | angle['Right']),deviation['High'])
]

#Step 4:Build & Simulate the control System
deviation_ctrl=ctrl.ControlSystem(rules)
deviation_sim=ctrl.ControlSystemSimulation(deviation_ctrl)

#input values
deviation_sim.input['distance']=1.04
deviation_sim.input['angle']=30

#Compute the result
deviation_sim.compute()
print(deviation_sim.output['deviation'])

#visualize the result
deviation.view(sim=deviation_sim)