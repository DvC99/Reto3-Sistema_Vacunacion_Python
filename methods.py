from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

#Lectura de datos
def registrar():
  nombre = input("Digite el nombre:\n")
  apellido = input("Digite el apellido:\n")
  genero = input("Diga si es del genero, hombre o mujer:\n")
  edad = input("Digite su fecha de nacimiento separada por / y con foramto(Y/m/d):\n")
  sangre = input("Digite el tipo de sangre:\n").upper()
  peso = input("Digite su pero en kilogramos:\n")
  cedula = input("Digite el numero de su cedula:\n")
  return nombre,apellido,genero, edad,sangre, peso, cedula
#Numeros primos
def numPrimo(num):
  for n in range(2, num):
    if num % n == 0:
      return False
  return True
#Calculo de la edad en años, meses y dias
def calcEdad(edad):
  years = int(edad.split("/")[0])
  meses = int(edad.split("/")[1])
  dias = int(edad.split("/")[2])
  edad = relativedelta(datetime.now(), datetime(years, meses, dias))
  return edad.years, edad.months, edad.days
#Se calcula la edad en dias
def edadDias(years, meses, dias):
  return(dias+(meses*31)+(years*365))
#Se verifica que los dos ultimos digitos de la cedula son primos
def ceduPrima(cedula): 
  return numPrimo(int(cedula[-2]+cedula[-1]))
#Calculo de las fechas de las citas  
def fechaCita(edadDias, denominador):
  fecha = (datetime.now() + timedelta(days=(edadDias/denominador))).strftime("%Y/%m/%d")
  #return( "Su cita será en el mes "+fecha.split("/")[1]+"y en el dia "+fecha.split("/")[2] )
  return( "Su cita será el:  "+fecha+"\n")
#Calcular la contraseña
def makePassw(nombre, apellido, cedula):
  return( nombre[0]+nombre[1]+apellido[0]+apellido[1]+cedula )