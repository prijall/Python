import numpy as np

#@ Random Sample for output:
layer_outputs = [4.8, 1.21, 2.385]

#@ Converting the output into exponential:
exponential_values=np.exp(layer_outputs)

#@Printing to see exponential values:
#print(exponential_values)

#@ Normalizing the values:
normalized_value=exponential_values/np.sum(exponential_values)

#@Printing to see normalized values:
#print(normalized_value)

#@ The sum of the normalized values must always be 1.
print('Sum of Normalized Values:', np.sum(normalized_value))