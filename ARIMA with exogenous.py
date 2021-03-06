import pandas as pd
import seaborn as sns
import statsmodels.api as sm

#calculate mape
def mape(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

#calculate rmse
def rmse(y_true, y_pred):
    return np.sqrt(((y_pred - y_true) ** 2).mean())

# main arima function    
def arima_x(df1,df2):
    Y = np.log(df1)
    X = np.log(df2)
    results = sm.tsa.ARIMA(Y, order = (2,1,1), exog = X).fit()
    coef = results.params
    fitted = pd.Series(results.fittedvalues)
    MAPE = mape(np.exp(Y),np.exp(fitted))
    RMSE = rmse(np.exp(Y),np.exp(fitted))
    coef = results.params
    plt.plot(np.exp(Y))
    plt.plot(np.exp(fitted), color='red')
    plt.title('MAPE: %.4f'% MAPE)
    print(results.summary())
    return MAPE, RMSE, coef
