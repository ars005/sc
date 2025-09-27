#triangular Membership Function
import numpy as np
import matplotlib.pyplot as plt

def triangular(x,a,b,c):
    return np.maximum(0,np.minimum((x-a)/(b-a),(c-x)/(c-b)))
#2. trpezoidal membership function
def trapezoidal(x,a,b,c,d):
    return np.maximum(0,np.minimum(np.minimum((x-a)/(b-a),1),(d-x)/(d-c)))
#3.gaussian membersip fuction
def gaussian(x,mean,sigma):
    return np.exp(-0.5*((x-mean)/sigma)**2)
#4. generalized bell-shaped membership function
def generalized_bell(x,a,b,c,):
    return 1 / (1+np.abs((x-c)/a)**(2*b))
#5. sigmoid membership function
def sigmoid(x,a,c):
    return 1 / (1+np.exp(-a*(x-c)))


#plot All membership  functions
x = np.linspace(0,10,1000)

plt.figure(figsize=(10,6))

plt.plot(x,triangular(x,2,5,8), label="Triangular")
plt.plot(x,trapezoidal(x,1,3,6,8), label="Trapezoidal")
plt.plot(x,gaussian(x,mean=5,sigma=1.2), label="Guassian")
plt.plot(x,generalized_bell(x,2,5,8), label="Generalized_Bell")
plt.plot(x,sigmoid(x,a=1,c=5), label="Sigmoid")

plt.title("Fuzzy Membership Fuction (From Starch)")
plt.xlabel("Input(x)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()

