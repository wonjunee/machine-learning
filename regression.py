from sklearn import linear_model

clf = linear_model.LinearRegression()
clf.fit([[0,0],[1,1],[2,2]],[0,1,2])

print clf.coef_

### Import LinearRegression, create regression
### and fit it to the training data

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(ages_train, net_worths_train)


print "r-squared score:", reg.score(ages_test, net_worths_train)