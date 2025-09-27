x = [0.8, 0.6, 0.4]#[ 0.2, 0.6, 0.4]
w = [0.1, 0.3, -0.2] #[ 0.3, 0.7, 0.5]
b = 0.35 # 0.45
y = 0
for i in range(len(x)):
   y+=x[i]*w[i]
y=y+b
print(y)

import numpy as np
class ActivationF :
 def bnsf(self, x):    #binary sigmoid function
    return 1/(1+np.exp(-x))

 def bpsf(self, x):        #bipolar sigmoidal function
    return -1+2/(1+np.exp(-x))
 
 def tanh(self, x):
    return (np.exp(x) - np.exp(-x) / np.exp(x) + np.exp(-x))

def main():
    binary = ActivationF().bnsf(y)
    print("\nThe output, after applying the binary sigmoidal function is:")
    print(round(binary,3))  #rounds off the answer by 3 decimal places
    bipolar = ActivationF().bpsf(y)
    print("\nThe output, after applying the bipolar sigmoidal function is:")
    print(round(bipolar,3))  #rounds off the answer by 3 decimal
    tangent = ActivationF().tanh(y)
    print("\nThe output, after applying the tangent function is:")
    print(round(tangent,3))  #rounds off the answer by 3 decimal places

if __name__ =="__main__":
    main() 



