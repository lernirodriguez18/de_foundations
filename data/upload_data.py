import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine('postgresql://foundations:foundations@postgres_service:5432/foundations_db') #postgres_service
connection = engine.connect()

df = pd.read_csv("transf-autos-2000-01-2022-04.csv", delimiter=",")

df_prov = df[['provincia_id','provincia_transferencia','letra_provincia_transferencia']].drop_duplicates()
df_prov.columns = ['id','nombre','letra']

df_transf = df[['anio_transferencia','mes_transferencia','provincia_id','cantidad_transferencias']]
df_transf.columns = ['anio','mes','id_provincia','cantidad']


truncate_query = sqlalchemy.text("TRUNCATE TABLE provincias,transferencias")
connection.execution_options(autocommit=True).execute(truncate_query)


df_prov.to_sql('provincias',con=engine,if_exists='append',index=False)
df_transf.to_sql('transferencias',con=engine,if_exists='append',index=False)


