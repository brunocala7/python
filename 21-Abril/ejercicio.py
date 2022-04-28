import pandas as pd
import os 
print("hola \n")
path = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(path + "/informacion.csv",sep=";",engine="python",encoding="latin-1")
df.set_index("Codigo")
df1 = df.drop_duplicates()
df1.to_csv(path + "/archivo1.csv",index=False)

df2 = pd.concat([df[:300],df[-200:]])
df2.to_csv(path + "/archivo2.csv",index=False)
print(df2)

df3 = df.loc[[1,5,12,36]]
df3.to_csv(path + "/archivo3.csv",index=False)

print(list(df.columns))

print(df["Nombre"].values)


"""
df = pd.read_csv("datos_nomivac_covid19.csv")
df = pd.read_csv("datos_nomivac_covid19.csv",sep=";",engine="python")
print(df)
print(list(df.columns))
print(list(df.index))
print(df['grupo_etario'])
df.loc[0:1000]
df.loc[[1,5,8]]
dfConIndiceDNI = df.set_index('DNI')
df['sexo'].value_counts()
df_2 = df.drop_duplicates()
df.to_csv("nuevo.csv")
"""
