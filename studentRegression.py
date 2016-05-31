from sklearn import linear_model

def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
	clf = linear_model.LinearRegression()
	clf.fit(ages_train,net_worths_train)

	reg =  clf.coef_
    
    return reg