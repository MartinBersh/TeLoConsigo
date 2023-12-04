while True:
  temperature = float(input("Ingresar temperatura: "))
  scale = input("Eliga la unidad de medida ingresada: Ferenheit(F), Celsius(C) o Kelvin(K)): ").lower()
  conversion = input("Eliga la unidad a la que quiere convertir su unidad: Ferenheit(F), Celsius(C) o Kelvin(K)): ").lower()

  if scale == "f":
    if conversion == "c":
      celsius = (temperature - 32) * 5/9
      print(f"Temperatura en Celsius: {celsius}")
    elif conversion == "k":
      kelvin = (temperature - 32) * (5/3) + 273.15
      print(f"Temperatura en Kelvin: {kelvin}")
    else:
      print("Escala invalida")
  elif scale == "c":
    if conversion == "f":
      farenheit = temperature * 1.8 + 32
      print(f"Temperatura en Fahrenheit: {farenheit}")
    elif conversion == "k":
      kelvin2 = temperature + 273.15
      print(f"Temperatura en Kelvin: {kelvin2}")
    else:
      print("Escala invalida")
  elif scale == "k":
    if conversion == "f":
      farenheit2 = (temperature - 273.15) * (9/5) + 32
      print(f"Temperatura en Fahrenheit: {farenheit2}")
    elif conversion == "c":
      celsius2 = temperature - 273.15
      print(f"Temperatura en Celsius: {celsius2}")
    else:
      print("Escala invalida")
  else:
    print("Escala ingresada no es valida")

  seguir_convirtiendo = input("¿Desea realizar otra conversion? si o no: ").lower()
  if seguir_convirtiendo != "si":
    break

print("Gracias por usar el convertidor de temperatura")
