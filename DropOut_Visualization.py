import numpy as np

dropout_rate=0.2
example_output=np.array([0.27, -1.03, 0.67, 0.99, 0.05,
-0.37, -2.01, 1.13, -0.07, 0.73])

print(f'Sum Initial {sum(example_output)}')

sums=[]

for i in range(10000):
    example_output2=example_output * np.random.binomial(1, 1-dropout_rate, example_output.shape)/(1- dropout_rate)
    sums.append(sum(example_output2))


print(f' Mean Sum {np.mean(sums)}')
