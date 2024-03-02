import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate=learning_rate
        self.iterations= iterations
        self.weight= None 
        self.bias=None
    
    def fit(self, X, y):
        num_samples, num_features=X.shape
        self.weight=np.zeros(num_features)
        self.bias=0

