### Import LinearRegression, create regression
### and fit it to the training data

from sklearn.linear_model import LinearRegression
reg = LinearRegression()

x = [[0],[1],[2]]
y = [1,3,5]
reg.fit(x,y)

print "coefficieents:", reg.coef_
print "intercept:", reg.intercept_
print "score:", reg.score(x,y)