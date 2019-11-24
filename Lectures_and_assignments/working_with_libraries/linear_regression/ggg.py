import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

x0 =  np.arange(0, 30, 1) # this is the independent variable
y0 =  12.1 + 0.23 * x0

noise = (np.random.uniform(-3,3,size=30))

yn = y0 + noise # this will be the dependen variable

df = pd.DataFrame({'x0':x0,'yn':yn})
df.head()

model = smf.ols(formula="yn ~ x0",data=df)

print(reveal_type(model))
