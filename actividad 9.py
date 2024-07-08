#9

nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Alumno:", nombre, apellido)
print("Promedio:", promedio)
