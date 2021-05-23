import methods as meth

nombre, apellido, genero, edad, sangre, peso, cedula = meth.registrar()
years, meses, dias = meth.calcEdad(edad)
edadDias = meth.edadDias(years, meses, dias)
clave = meth.makePassw(nombre, apellido, cedula)
if(years > 60):
  if(genero == "mujer"):
    if(sangre == "O+"):
      if(peso > "70"):
        if(meth.ceduPrima(cedula)):
          denominador = 150
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:
          denominador = 80
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)
    elif(sangre == "A-"):
      if(peso > "70"):
        if(meth.ceduPrima(cedula)):
          denominador = 200
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:
          denominador = 45
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)
    else:
      if(peso > "70"):
        if(meth.ceduPrima(cedula)):      
          denominador = 175
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:    
          denominador = 100
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)

  elif(genero == "homnbre"):
    if(sangre == "O+"):
      if(peso > "80"):
        if(meth.ceduPrima(cedula)):
          denominador = 180
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:
          denominador = 90
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)
    elif(sangre == "A-"):
      if(peso > "80"):
        if(meth.ceduPrima(cedula)):
          denominador = 210
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:
          denominador = 40
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)
    else:
      if(peso > "80"):
        if(meth.ceduPrima(cedula)):      
          denominador = 145
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)        
        else:    
          denominador = 105
          print(meth.fechaCita(edadDias, denominador) )
          print("\n Su clave de acceso es: "+clave)
  else:
    print("Genero no valido")
else:
  denominador = 145
  print(meth.fechaCita(edadDias, denominador) )
  print("Su clave de acceso es: "+clave)