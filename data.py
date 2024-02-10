import pandas as pd
import constants as C

### import data
def get_df(excel_name, sheet_name, unwanted_cols):
    excel_name = excel_name
    sheet_name = sheet_name
    unwanted_cols = unwanted_cols
    df = pd.read_excel(excel_name, sheet_name, engine='openpyxl', index_col='Name')
    df = df.drop(columns=unwanted_cols)
    return df

df_main = get_df('Datenanalyse.xlsx', 'SPD', C.unwanted_cols_SPD)
df_wahlbet = get_df('Datenanalyse.xlsx', 'BTW 2021', C.unwanted_cols_wahlbet)
df_main = df_main.join(df_wahlbet, how='inner')
df_main.rename(columns=C.newname_cols_SPD, inplace=True)

for file, feature in C.features_needed:
     df_new = pd.read_csv(file, index_col="Gebiet")
     filt = (df_new['Sachmerkmal'] == feature[1])
     df_new = df_new[filt]
     df_new[feature[-1]] = df_new[feature[0]]
     df_new = df_new.loc[:, [feature[-1]]]
     df_main = df_main.join(df_new, how='inner')

### clean and scale data
df_main = df_main.convert_dtypes()
for col in C.cols_comma:
    df_main[col] = df_main[col].str.replace(',','.')
for col in C.cols_to_float:
    df_main[col] = df_main[col].astype(float)

df_quote = df_main.drop(index=['Stadt Leipzig'])

for col in C.cols_to_scale:
    df_quote[col] = df_quote[col] / df_quote['Einwohner']

# skaliere 'Arbeitslose Frauen' separat: Anteil AF an Erwerbsfähigen, nicht Einwohnern
df_new = pd.read_csv('Arbeitslose.csv', index_col="Gebiet")
filt = (df_new['Sachmerkmal'] == 'Arbeitslose insgesamt')
df_new = df_new[filt]
df_new['2022'] = df_new['2022'].astype(float)
df_quote['Arbeitslose Frauen'] = df_quote['Arbeitslosenquote'] * df_quote['Arbeitslose Frauen'] / df_new['2022']

for col in C.cols_to_hundred:
    df_quote[col] = df_quote[col].map(lambda x: x * 100)
df_quote['Haushaltseinkommen'] = df_quote['Haushaltseinkommen'].apply(lambda x: x/100)

# df_diff für wählerzuwachs
df_diff = df_quote.copy()
df_diff['LTW'] = df_diff['BTW'] - df_diff['LTW']
df_diff['KMW'] = df_diff['BTW'] - df_diff['KMW']

