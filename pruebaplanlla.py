import matplotlib.pyplot as plt

empleados = []

for i in range(5):
    try:
        nombreEmpleado = input("Ingrese el nombre del empleado {}: ".format(i + 1))
        if not nombreEmpleado:
            raise ValueError("El nombre no puede estar vacío.")
        
        cedula = input("Ingrese la cédula del empleado {}: ".format(nombreEmpleado))
        if not cedula:
            raise ValueError("La cédula no puede estar vacía.")
        
        # Entrada de edad con validación
        try:
            edad = int(input("Ingrese la edad del empleado {}: ".format(nombreEmpleado)))
            if edad <= 0:
                raise ValueError("La edad debe ser un número positivo.")
        except ValueError as e:
            print("Error en la entrada de edad:", e)
            continue

        # Entrada de horas trabajadas con validación
        try:
            horasTrabajadas = float(input("Ingrese las horas trabajadas del empleado {}: ".format(nombreEmpleado)))
            if horasTrabajadas <= 0:
                raise ValueError("Las horas trabajadas deben ser un número positivo.")
        except ValueError as e:
            print("Error en la entrada de horas trabajadas:", e)
            continue

        # Entrada de pago por hora con validación
        try:
            pagoHora = float(input("Ingrese el pago por hora del empleado {}: ".format(nombreEmpleado)))
            if pagoHora <= 0:
                raise ValueError("El pago por hora debe ser un número positivo.")
        except ValueError as e:
            print("Error en la entrada de pago por hora:", e)
            continue

        # Cálculo de salario bruto y deducciones
        salarioBruto = horasTrabajadas * pagoHora
        seguroSocial = salarioBruto * 0.0975
        seguroEducativo = salarioBruto * 0.0125
        impuestoRenta = salarioBruto * 0.10
        totalDeducciones = seguroSocial + seguroEducativo + impuestoRenta
        sueldoPagar = salarioBruto - totalDeducciones

        # Guardar datos en el diccionario del empleado
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
        empleados.append(empleado)

    except ValueError as e:
        print("Error en los datos del empleado:", e)
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
    
# Obtener el usuario con el mayor sueldo y mayor edad
empleado_mayor_sueldo = max(empleados, key=lambda e: e["sueldoPagar"])
empleado_mayor_edad = max(empleados, key=lambda e: e["edad"])

# Mostrar los resultados en la terminal
print("\nEmpleado con el mayor sueldo a pagar:")
print("Nombre: {}, Cédula: {}, Sueldo a Pagar: {:.2f}".format(
    empleado_mayor_sueldo["nombre"], empleado_mayor_sueldo["cedula"], empleado_mayor_sueldo["sueldoPagar"]))

print("\nEmpleado con la mayor edad:")
print("Nombre: {}, Cédula: {}, Edad: {}".format(
    empleado_mayor_edad["nombre"], empleado_mayor_edad["cedula"], empleado_mayor_edad["edad"]))

# Generación de gráficos
nombres = [e["nombre"] for e in empleados]
edades = [e["edad"] for e in empleados]
sueldos = [e["sueldoPagar"] for e in empleados]

plt.figure(figsize=(13, 6))

# Gráfico Nombre vs Edad
plt.subplot(1, 2, 1)
plt.bar(nombres, edades, color='skyblue')
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.title('Nombre vs Edad')

# Gráfico Nombre vs Sueldo
plt.subplot(1, 2, 2)
plt.bar(nombres, sueldos, color='salmon')
plt.xlabel('Nombre')
plt.ylabel('Sueldo por pagar')
plt.title('Nombre vs Sueldo por pagar')

plt.tight_layout()
plt.show()