import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

class QuadraticModel:
    def fit(self, x, y):
        x = pd.DataFrame(x)
        quadratic = PolynomialFeatures(degree=2)
        quad_features = quadratic.fit_transform(x)
        quad_model = LinearRegression().fit(quad_features, y)
        y_pred = quad_model.predict(quad_features)
        self.a = quad_model.coef_[2]
        self.b = quad_model.coef_[1]
        self.c = quad_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.a*x**2 + self.b*x + self.c
       
    def plot_model(self, xmin, xmax):
        xvals = range(xmin, xmax+1)
        yvals = [self.predict(x) for x in xvals]
        plt.plot(xvals, yvals, color='black')
        
    def print_model_info(self):
        a = self.a
        b = self.b
        c = self.c
        rsquared = self.rsquared
        print('QuadraticModel')
        print(f'Parameters: a = {a:.2f}, b = {b:.2f}, c = {c:.2f}')
        print(f'Equation: y = {self.a:.2f}x² + {self.b:.2f}x + {self.c:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')