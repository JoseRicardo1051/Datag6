import mysql.connector

#creo conexiÃ³n a mi bd
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db_g6'
)

print(f'estas conectado a la base de datos {connection.database}')

#insertar datos en mi tabla
# alumno_cursor = connection.cursor()
# alumno_cursor.execute("insert into alumno(nro_documento,nombre) values('1002','Jesus Lopez')")
# connection.commit()
# print("alumno insertado")

alumno_cursor_select = connection.cursor()
alumno_cursor_select.execute("select nro_documento,nombre from alumno")
resultado = alumno_cursor_select.fetchall()
for registro in resultado:
    print('*'*50)
    print(f'DNI : {registro[0]}')
    print(f'NOMBRE : {registro[1]}')

connection.close()
#completar delete update
