import matplotlib.pyplot as plt
import constants as C
import data as D
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF
import pandas as pd

### simple functions
# ausreißer für merkmal 'col'
def find_significants(col, df = D.df_quote):
    dfcap = df.copy()
    if "Stadt Leipzig" in df.index:
        dfcap = df.drop(index='Stadt Leipzig')
    deviation = 2 * dfcap[col].std()
    mn = dfcap[col].mean()
    filt = ( abs(dfcap[col] - mn) > deviation )
    print(f'__Mittelwert__: \n{mn:.2f} \n\n__2*sigma__:\n{deviation:.2f} \n\n__Abweichler__: \n{dfcap[filt][col]}')

# korrelationskoeffizient der merkmale col1, col2
def correlation(col1, col2, df = D.df_quote):
    dfcap = df.copy()
    if "Stadt Leipzig" in df.index:
        dfcap = df.drop(index='Stadt Leipzig')
    first = dfcap[col1]
    second = dfcap[col2]
    cor = first.corr(second)
    print(f"__Korrelationskoeffizient für {col1} und {col2}__: \n{cor:.2f}")

# alle signifikanten korrelationskoeffizienten (ab +/-.3) der wahlergebnisse mit allen merkmalen
def significant_correlations(df = D.df_quote):
    # only interested in numerical variables
    dfcap = df.select_dtypes(include=['int', 'float'])
    dependents = C.cols_dependent
    independents = C.cols_independent
    threshold = .3
    if "Stadt Leipzig" in df.index:
        dfcap = df.drop(index='Stadt Leipzig')

    for column1 in dependents:
        for column2 in independents:
            corr = dfcap[column1].corr(dfcap[column2])
            if abs(corr) > threshold:
                print(f"__Korrelationskoeffizient für {column1} und {column2}__: \n{corr:.2f}")

# simple plot
def plot_ergebnis_feature(y, x='', frame = D.df_quote, bezirk=''):
    df = frame
    if bezirk:
        filt = df["Bezirk"] == bezirk
        df = df[filt]

    if x:
        plt.scatter(df[x], df[y])
        plt.title(str(y) + ' for ' + str(x))
    else:
        plt.scatter(df.index, df[y])
        plt.xticks(rotation=45, ha='right')
        plt.title(str(y) + ' nach Stadtteil ')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

### regression prep
# check pairwise correlation coefficients
def filter_params_by_corr(frame = D.df_quote):
    params = C.cols_independent
    threshold = .6
    # initialize array of dropped columns
    dropped = []
    for col1 in params:
        for col2 in params:
            corr = abs(frame[col1].corr(frame[col2]))
            if col1 != col2 and col2 not in dropped and corr > threshold:
                #print(f'correlation {col1} with {col2} is {corr:.2f}')
                if col1 not in dropped:
                    dropped.append(col1)
                params = [x for x in params if x != col1]
    return params

# VIF (variance inflation factor) for potential columns
def filter_params_by_VIF(frame = D.df_quote):
    params = filter_params_by_corr(frame) # C.cols_independent
    X = sm.add_constant(frame[params])
    threshold = 4

    vif_data = pd.DataFrame()
    vif_data.index = X.columns
    vif_data["VIF"] = [VIF(X.values, i) for i in range(X.shape[1])]
    print(vif_data)

    params = [x for x in params if vif_data.loc[x,"VIF"] < threshold]

    print('\nParameters left after filtering:')
    print(params)
    print('\n')
    return params

### OLS regression
def regression(wahl = 'BTW', frame = D.df_quote, drop=[]):
    params = filter_params_by_VIF(frame)
    params = [x for x in params if x not in drop]

    y = frame[wahl]
    X = frame[params]
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    print(model.summary())

