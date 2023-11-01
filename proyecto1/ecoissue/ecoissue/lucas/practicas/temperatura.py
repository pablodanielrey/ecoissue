#Conversor de temperaturas 


while True:
    temperatura = input("La temperatura es Celcius(c), Fahrenheit(f) o Kelvin(k): ")
    #### Se convierte de Fahrenheit a Celcius o Kelvin #######

    if temperatura == str("f"):
        temperaturaF = input("Quiere converitr a Celcius(c) o a Kelvin(k)? ")
        if temperaturaF == str("c"):
            gradosF = float(input("Ingrese que temperatura hace en Fahrenheit: "))
            print("Convirtiendo la temperatura en Celcius....")
            tempC = 5/9 * (gradosF - 32) # Formula para convertir Fahrenheit en Celcius
            print("La temperatura en Celcius es " , tempC)
            break
        else:
            gradosF = float(input("Ingrese que temperatura hace en Fahrenheit: "))
            print("Convirtiendo la temperatura en Kelvin....")
            tempK = (gradosF - 32) * 5/9 + 273.15 # Formula para convertir Fahrenheit en Kelvin
            print("La temperatura en Kelvin es " , tempK)
            break
    #### Se convierte de Celcius a Fahrenheit o Kelvin #######

    elif temperatura == str("c"):
        temperaturaC = input("Quiere convertir a Fahrenhit(f) o a Kelvin(k)? ")
        if temperaturaC == str("f"):
            gradosC = float(input("Ingrese que temperatura hace en Celcius: "))
            print("Convirtiendo la temperatura en Fahrenheit....")
            tempF = (gradosC * 9/5) + 32  # Formula para convertir Celcius en Fahrenheit
            print ("La temperatura en Fahrenheit es " , tempF)
        else:
            gradosC = float(input("Ingrese que temperatura hace en Celcius: "))
            print("Convirtiendo la temperatura en Kelvin....")
            tempK = gradosC + 273.15 # Formula para convertir Fahrenheit en Kelvin
            print("La temperatura en Kelvin es " , tempK)
            break

    #### Se convierte de Kelvin a Fahrenheit o Celsius #######    
    else:
        temperaturaK = input("Quiere convertir a Fahrenhit(f) o a Celsius(c)? ")
        if temperaturaK == str("f"):
            gradosK = float(input("Ingrese que temperatura hace en Kelvin: "))
            print("Convirtiendo la temperatura en Fahrenheit....")
            tempK = (gradosK - 273.15)*9/5 + 32  # Formula para convertir kelvin en Fahrenheit
            print ("La temperatura en Fahrenheit es " , tempK)
        else:
            gradosK = float(input("Ingrese que temperatura hace en Kelvin: "))
            print("Convirtiendo la temperatura en Celcius....")
            tempK = gradosK - 273.15 # Formula para convertir Kelvin a Celsius
            print("La temperatura en Celsius es " , tempK)
            break
print("Programa terminado")