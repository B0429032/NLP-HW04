import pandas as pd
import csv

df=pd.read_csv('C:\Users\Kunying\Desktop\冠勳資料\109-2課程\線上校外實習\HW03\HW02.csv')
df_sum = df.groupby('AskPrice')['AskQuantity'].sum()
df_sum.to_csv('C:\Users\Kunying\Desktop\冠勳資料\109-2課程\線上校外實習\HW03\HW03.csv')
