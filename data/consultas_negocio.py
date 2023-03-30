from sqlalchemy import create_engine

engine = create_engine('postgresql://foundations:foundations@postgres_service:5432/foundations_db')

print('\n ----Respuestas de Negocio---- \n')

res = engine.execute('select anio,sum(cantidad) cantidad from transferencias group by anio order by 2 desc limit 1').fetchall()
print('1. ¿Cual fue el año donde mas transferencias se realizaron?')
print('En el año {} se realizaron {} transferencias \n'.format(res[0][0],res[0][1]))

res = engine.execute('select pr.nombre,sum(tr.cantidad) cantidad from transferencias tr join provincias pr on tr.id_provincia = pr.id group by pr.nombre order by 2 desc limit 5').fetchall()
print('2. ¿Cuales son las 5 provincias que mas transferencias realizaron en este periodo de tiempo?')
for item in res:
    print('{} realizo {} transferencias'.format(item[0],item[1]))
print('\n')

res = engine.execute('select pr.nombre,sum(tr.cantidad) cantidad from transferencias tr join provincias pr on tr.id_provincia = pr.id group by pr.nombre order by 2 limit 3').fetchall()
print('3. ¿Cuales son las 3 provincias que menos transferencias realizaron en este periodo de tiempo?')
for item in res:
    print('{} realizo {} transferencias'.format(item[0],item[1]))
print('\n')

res = engine.execute('select mes,sum(cantidad) cantidad from transferencias where anio = 2019 group by mes order by 2 desc limit 1').fetchall()
print('4. ¿Que mes del año 2019 fue donde menos transferencias se realizaron?')
print('En el año 2019, el mes nro {} fue donde mas transferencias se realizaron. Se realizaron {} transferencias \n'.format(res[0][0],res[0][1]))

res = engine.execute('select anio,sum(cantidad) cantidad from transferencias where id_provincia = 6 group by anio order by 1').fetchall()
print('5. Mostrar evolucion de transferencias de la provincia de Buenos Aires año a año.')
for item in res:
    print('Año {} - Tansferencias: {} '.format(item[0],item[1]))

