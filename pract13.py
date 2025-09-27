import numpy as np
class HebbruleNN:
  def __init__(self, input_size, learning_rate=0.01):
    #Initialize weights randomly or to zeros
    self.weights = np.zeros(input_size)
    self.bias = 0
    self.learning_rate = learning_rate

  def train(self, inputs, targets):
    for i in range(len(inputs)):
      input_vector = inputs[i]
      target_output = targets[i]

      #HebbruleNN weight update rule
      delta_weights = self.learning_rate * input_vector * target_output
      self.weights += delta_weights

      #HebbruleNN bias update rule
      delta_bias = self.learning_rate * target_output
      self.bias += delta_bias

  def predict(self, input_vector):
    #Activation function (e.g., step function for binary output)
    net_input =np.dot(input_vector, self.weights) + self.bias
    return 1 if net_input >= 0 else 0 #Example step Function

#Example Usage:
inputs = np.array([[1, 1], [1, -1], [-1, 1], [-1,-1]]) #Example inputs
targets1 = np.array([1, 1, 1, -1]) #Example targets(e.g., for an AND-like function with bipolar outputs)

network = HebbruleNN(input_size=2)
network.train(inputs, targets1)

print("Final Weights:", network.weights)
print ("Final Bias.", network.bias)