bisiesto = bool
año = int(input("ingresa un año entre 1900 y 2199 a ver si es bisiesto "))
años_bisiestos=0
if año <= 2199 and año > 1900: #si el valor es mayor que 2199 y menor que 1900 pasa que el año no es valido
    if año / 4 == año//4: #si la division entre 4 es igual a la division entera entre 4 sigue el programa (puede ser bisiesto)
        if año / 400 == año//400: #si la division entre 400 es igual a la division entera entre 400 sigue el programa (es bisiesto)
            bisiesto = True #si bisiesto es true el año es bisiesto
        elif año % 100 == 0: #si modulo de 100 es igual a 0 el año no es bisiesto (el año es multiplo de 100)
            bisiesto= False #si bisiesto es false el año no es bisiesto
        else:
            bisiesto = True
    else:
        bisiesto= False
    if bisiesto == True:
        print (f"el año {año} es bisiesto")   
    else:
        print (f"el año {año} no es bisiesto")
    for num in range(1900, año+1, 4): #toma en cuenta los años bisiestos
        if num % 4 ==0: #si el modulo de 4 es igual a cero este año siempre es bisiesto
            años_bisiestos+=1 #suma el año bisiesto a la lista
    if años_bisiestos !=1:
        if año >= 2100: #esto evita que se tome el 2100 como año bisiesto
            print (f"El numero de años bisiestos entre 1900 y {año} es {(años_bisiestos)-2}")
        else:
            print (f"El numero de años bisiestos entre 1900 y {año} es {(años_bisiestos)-1}")
    else:
        print (f"El numero de años bisiestos entre 1900 y {año} es {(años_bisiestos)}")
else:
    print("Este año no es valido")