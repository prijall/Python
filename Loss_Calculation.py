import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()

#@ Dense Layer:
class Dense_Layer:

    def __init__(self, n_inputs, n_neurons):
        self.weights=0.01* np.random.randn(n_inputs, n_neurons)
        self.biases=np.zeros(1, n_neurons)

    
    def forward(self, inputs):
        self.output=np.dot(inputs, self.weights) +self.biases


#@ Activation function:
class ReLU():
    def forward(self, inputs):
        self.output=np.maximum(0, inputs)


class Softmax():
    def forward(self, inputs):
        exp_values=np.exp(inputs-np.max(inputs, axis=1, keepdims=True))
        probabilities=exp_values/np.sum(exp_values, axis=1, keepdims=True)
        self.output=probabilities

    
#@ Loss Calculation:
class Loss:
    def calculate(self, output, y):
        losses=self.forward(output, y)
        data_loss=np.mean(losses)
        return data_loss
    

# types:
class CategoricalCrossEntropy(Loss):
    def forward(self, y_pred, y_true):
        samples=len(y_pred)

        # to prevent division by 0:
        y_pred_clipped=np.clip(y_pred, 1e-7, 1-1e-7)

        #for categorical labels:
        if len(y_true.shape)==1:
                    correct_confidence=y_pred_clipped[range(samples), y_true]
        
        # for one hot encoding:
        elif len(y_true.shape)==2:
             correct_confidence=np.sum(y_pred_clipped * y_true, axis=1)

        negative_log_likelihood=-np.log(correct_confidence)
        return negative_log_likelihood