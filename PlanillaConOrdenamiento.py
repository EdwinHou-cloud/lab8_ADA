"""Realice un programa en Python que calcule la planilla de 10 empleados 
de una compañía para obtener las siguientes deducciones: seguro social 9.75 %, 
seguro educativo 1.25 %, impuesto sobre la renta 10 %."""
#InicioAlgoritmo

#Inicializamos la lista empleados, para guardar los datos de cada empleado
empleados= []

j=1 #inicializa la variable j en 1

#Bucle for para solicitar los datos de los 10 empleados
for i in range(1):
    nombreEmpleado= input("Ingrese el nombre del empleado {}: ".format(j))
    cedula= input("Ingrese la cedula del empleado {}: ".format(nombreEmpleado))
    horasTrabajadas= float(input("Ingrese las horas trabajadas del empleado {}: ".format(nombreEmpleado)))
    pagoHora= float(input("Ingrese el pago por hora del empleado {}: ".format(nombreEmpleado)))
    print("\n")
    j=j+1 #Incrementa el valor de j en 1
    
    #Calculo de salario bruto
    salarioBruto = horasTrabajadas * pagoHora
    
    #Calculo de todas las deducciones
    seguroSocial = salarioBruto * 0.0975
    seguroEducativo = salarioBruto * 0.0125
    impuestoRenta = salarioBruto * 0.10
    totalDeducciones = seguroSocial + seguroEducativo + impuestoRenta

    #Calculo de sueldo por pagar
    sueldoPagar = salarioBruto - totalDeducciones
    
    #Creamos el diccionario empleado para almacenar los datos de cada empleado
    empleado = {"nombre": nombreEmpleado, 
                "cedula": cedula, 
                "horasTrabajadas": horasTrabajadas, 
                "pagoHora": pagoHora, 
                "salarioBruto": salarioBruto,
                "totalDeducciones": totalDeducciones,
                "sueldoPagar": sueldoPagar
    }
    #Agregamos el diccionario empleado en la lista empleados con el metodo append(), el cual agregara un elemento al final de una lista
    empleados.append(empleado) 

#Imprimir encabezado de la tabla
print("{:20} {:15} {:18} {:15} {:14} {:16} {:15}".format(
    'Nombre del empleado', 'Cedula', 'Horas trabajadas', 'Pago por hora', 'Salario bruto', 'Total de deducciones', 'Sueldo por pagar'))

#Imprimir la tabla con los datos de cada empleado
for empleado in empleados:
    print("{:20} {:15} {:15.2f} {:15.2f} {:15.2f} {:15.2f} {:15.2f}".format(empleado["nombre"],empleado["cedula"],empleado["horasTrabajadas"],empleado["pagoHora"],empleado["salarioBruto"],empleado["totalDeducciones"],empleado["sueldoPagar"]))
#FinAlgoritmo