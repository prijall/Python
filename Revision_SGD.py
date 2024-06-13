import numpy as np
import os
import sys
import nnfs

# Adding custom module's path to sys.pathsys.path.append(r"C:\Users\khadk\Desktop\DeepLearning\Code")
sys.path.append(r"C:\Users\khadk\Desktop\DeepLearning\Code")


from LayersofNeurons_part2 import Dense_layer
from ReLu_condition_Part2 import ReLu_Activation 
from Activation_Softmax_Loss_CategoricalCrossentropy import Activation_Softmax_Loss_CategoricalCrossentropy



from nnfs.datasets import spiral_data
nnfs.init()

class SGD:

    def __init__(self, learning_rate=1):
        self.learning_rate=learning_rate

    # For updating parameter:

    def update_params(self, Layer):
        Layer.weights+= - self.learning_rate * Layer.dweights
        Layer.biases+= - self.learning_rate * Layer.dbiases
        

X, y=spiral_data(samples=100, classes=3)
dense1=Dense_layer(2, 44)
activation1=ReLu_Activation()

dense2=Dense_layer(44, 3)
activation2=Activation_Softmax_Loss_CategoricalCrossentropy()

optimizer=SGD()


for epoch in range(10001):

    dense1.forward(X)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    loss=activation2.forward(dense2.output, y)

    predictions=np.argmax(activation2.output, axis=1)
    if len(y.shape)==2:
        y=np.argmax(y, axis=1)
    accuracy=np.mean(predictions==y)

    if not epoch % 100:
        print(f'epoch:{epoch}, ' + f'acc:{accuracy:.3f}, ' + f'loss: {loss:.3f}')


    #Backward Pass
    activation2.backward(activation2.output, y)
    dense2.backward(activation2.dinputs)
    activation1.backward(dense2.dinputs)
    dense1.backward(activation1.dinputs)

    # Update weights and biases:
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)