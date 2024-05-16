def perceptron(X, y):
    """This function is perceptron which accepts values 'X' as in input values whereas 'y' as target variables from the dataset"""
    w1=w2=b=1
    learning_rate=0.01

    for j in range(1000):
        for i in range(X.shape[0]):

            #condition:
            z=w1*X[i][0]+w2*X[i][1]+b
            
            if z*y[i]<0:
                w1=w1+learning_rate*y[i]+X[i][0]
                w2=w2+learning_rate*y[i]+X[i][2]
                b=b+learning_rate*y[i]
    return w1, w2, b