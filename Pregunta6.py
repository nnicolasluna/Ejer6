
import psycopg2 

conexion = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="airepick123", 
                    database="joelluna")
print("conexion exitosa")
bd = conexion.cursor()


sql="SELECT persona.departamento,avg(inscripcion.notafinal), CASE WHEN persona.departamento='LP' THEN avg(inscripcion.notafinal) WHEN persona.departamento='SC' THEN avg(inscripcion.notafinal) WHEN persona.departamento='03' THEN avg(inscripcion.notafinal) ELSE 0 END FROM persona, inscripcion WHERE persona.ci=inscripcion.ciestudiante group by persona.departamento;"
bd.execute(sql)
rows=bd.fetchall()

for row in rows:
    print(row)
    


