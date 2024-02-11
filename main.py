import pandas as pd
import constants as C
import functions as F
import data as D

# show all columns
pd.set_option('display.max_columns', None)
# show =2 decimal points
pd.set_option('display.float_format', '{:.2f}'.format)

#F.regression('BTW')#, drop=['Jugendquote','Haushaltseinkommen','Lebenszufriedenheit'])

print(D.df_quote.columns)