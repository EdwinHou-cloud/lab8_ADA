"""
Integrantes:
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		    8-1012-688
"""
import matplotlib.pyplot as plt

# Lista para almacenar la información de cada empleado como diccionarios
empleados = []

# Bucle para recopilar información de cinco empleados
for i in range(5):
    while True:  # Bucle para seguir pidiendo datos hasta que sean válidos
        try:
            # Entrada del nombre del empleado y validación
            nombreEmpleado = input("Ingrese el nombre del empleado {}: ".format(i + 1))
            if not nombreEmpleado or not nombreEmpleado.replace(" ", "").isalpha():
                raise ValueError("El nombre no puede estar vacío y debe contener solo letras.")
            
            # Entrada de la cédula del empleado y validación
            cedula = input("Ingrese la cédula del empleado {}: ".format(nombreEmpleado))
            if not cedula:
                raise ValueError("La cédula no puede estar vacía.")
            
            # Entrada y validación de la edad del empleado
            while True:  # Bucle para validar la edad
                try:
                    edad = int(input("Ingrese la edad del empleado {}: ".format(nombreEmpleado)))
                    if edad <= 0:
                        raise ValueError("La edad debe ser un número positivo.")
                    break  # Salir del bucle si la edad es válida
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para la edad.")

            # Entrada y validación de las horas trabajadas por el empleado
            while True:  # Bucle para validar las horas trabajadas
                try:
                    horasTrabajadas = float(input("Ingrese las horas trabajadas del empleado {}: ".format(nombreEmpleado)))
                    if horasTrabajadas <= 0:
                        raise ValueError("Las horas trabajadas deben ser un número positivo.")
                    break  # Salir del bucle si las horas son válidas
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para las horas trabajadas.")

            # Entrada y validación del pago por hora del empleado
            while True:  # Bucle para validar el pago por hora
                try:
                    pagoHora = float(input("Ingrese el pago por hora del empleado {}: ".format(nombreEmpleado)))
                    if pagoHora <= 0:
                        raise ValueError("El pago por hora debe ser un número positivo.")
                    break  # Salir del bucle si el pago es válido
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para el pago por hora.")

            # Si todas las entradas son válidas, se calcula el salario bruto
            salarioBruto = horasTrabajadas * pagoHora  # Cálculo de salario bruto
            seguroSocial = salarioBruto * 0.0975  # Seguro social del 9.75%
            seguroEducativo = salarioBruto * 0.0125  # Seguro educativo del 1.25%
            impuestoRenta = salarioBruto * 0.10  # Impuesto sobre la renta del 10%
            totalDeducciones = seguroSocial + seguroEducativo + impuestoRenta  # Suma total de las deducciones
            sueldoPagar = salarioBruto - totalDeducciones  # Sueldo final después de deducciones

            # Diccionario con la información del empleado
            empleado = {
                "nombre": nombreEmpleado,
                "cedula": cedula,
                "edad": edad,
                "horasTrabajadas": horasTrabajadas,
                "pagoHora": pagoHora,
                "salarioBruto": salarioBruto,
                "totalDeducciones": totalDeducciones,
                "sueldoPagar": sueldoPagar
            }
            empleados.append(empleado)  # Agregar el diccionario a la lista de empleados

            # Salir del bucle mientras se han ingresado correctamente todos los datos
            break

        except ValueError as e:
            print("Error:", e)
            print("Por favor, ingrese los datos nuevamente.\n")

# Imprimir encabezado de la tabla con bordes
print("_"*136)
print("|{:^25}|{:^15}|{:^18}|{:^15}|{:^15}|{:^22}|{:^18}|".format(
    'Nombre del empleado', 'Cédula', 'Horas trabajadas', 'Pago por hora', 'Salario bruto', 'Total de deducciones', 'Sueldo por pagar'))
print("|" + "_"*25 + "|" + "_"*15 + "|" + "_"*18 + "|" + "_"*15 + "|" + "_"*15 + "|" + "_"*22 + "|" + "_"*18 + "|")

# Imprimir la tabla con los datos de cada empleado
for empleado in empleados:
    print("|{:^25}|{:^15}|{:^18.2f}|{:^15.2f}|{:^15.2f}|{:^22.2f}|{:^18.2f}|".format(
        empleado["nombre"], empleado["cedula"], empleado["horasTrabajadas"], 
        empleado["pagoHora"], empleado["salarioBruto"], 
        empleado["totalDeducciones"], empleado["sueldoPagar"]))
    print("|" + "_"*25 + "|" + "_"*15 + "|" + "_"*18 + "|" + "_"*15 + "|" + "_"*15 + "|" + "_"*22 + "|" + "_"*18 + "|")

# Obtener el empleado con el mayor sueldo y el de mayor edad
empleado_mayor_sueldo = max(empleados, key=lambda e: e["sueldoPagar"])  # Empleado con mayor sueldo
empleado_mayor_edad = max(empleados, key=lambda e: e["edad"])  # Empleado con mayor edad

# Mostrar los resultados en la terminal
print("\nEmpleado con el mayor sueldo a pagar:")
print("Nombre: {}, Cédula: {}, Sueldo a Pagar: {:.2f}".format(
    empleado_mayor_sueldo["nombre"], empleado_mayor_sueldo["cedula"], empleado_mayor_sueldo["sueldoPagar"]))

print("\nEmpleado con la mayor edad:")
print("Nombre: {}, Cédula: {}, Edad: {}".format(
    empleado_mayor_edad["nombre"], empleado_mayor_edad["cedula"], empleado_mayor_edad["edad"]))

# Generación de gráficos
nombres = [e["nombre"] for e in empleados]  # Lista de nombres de empleados
edades = [e["edad"] for e in empleados]  # Lista de edades de empleados
sueldos = [e["sueldoPagar"] for e in empleados]  # Lista de sueldos a pagar de empleados

plt.figure(figsize=(13, 6))  # Tamaño de la figura

# Gráfico Nombre vs Edad
plt.subplot(1, 2, 1)  # Primera posición de gráfico
plt.bar(nombres, edades, color='skyblue')  # Barra de edad
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.title('Nombre vs Edad')

# Gráfico Nombre vs Sueldo
plt.subplot(1, 2, 2)  # Segunda posición de gráfico
plt.bar(nombres, sueldos, color='salmon')  # Barra de sueldo a pagar
plt.xlabel('Nombre')
plt.ylabel('Sueldo por pagar')
plt.title('Nombre vs Sueldo por pagar')

plt.tight_layout()  # Ajuste automático de espacios
plt.show()  # Mostrar gráficos
