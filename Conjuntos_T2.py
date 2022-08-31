from calendar import c
import os

#conjuntos 
cu = set ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
cv = set (["      "])
ca = set ([1,3,5,8,10,12])
cb = set ([2,3,4,6,8,14])

loop = True 
while loop:
    #Aqui se imprimen los datos de cada conjunto para que el usuario los conozca
    print("TAREA 2 EJEMPLOS DE CONJUNTOS 20110084")
    print("\nLos numeros del conjunto A son:",ca)
    print("Los numeros del conjunto B son:",cb)
    print("Los numeros del conjunto de tipo universo son:",cu)
    print("Los numeros del conjunto de tipo vacio son:",cv)
    print("\nQué opción deseas ejecutar:")
    #Aqui se imprime el menu con los tipos de ejemplos que puede seleccionar
    print("\nA) UNION ENTRE LOS CONJUNTOS A CON CONJUNTO B:")
    print("B) INTERSECCION DEL CONJUNTO A CON EL CONJUNTO B:")
    print("C) DIFERENCIA DE CONJUNTO A CON EL CONJUNTO B:")
    print("D) EL CONJUNTO A ES SUBCONJUNTO DEL CONJUNTO UNIVERSO?")
    print("E) EL CONJUNTO B ES SUBCONJUNTO DEL CONJUNTO UNIVERSO?")
    print("F) EL CONJUNTO UNIVERSO ES UN SUPERCONJUNTO DEL A?")
    print("G) EL CONJUNTO A Y EL B SON IGUALES?")
    print("H) LA DIFERENCIA SIMETRICA DE EL CONJUNTO UNIVERSO CON EL A ES:")
    print("X) SALIR:")
 
 
    opcion = input("\nESCOGE LA OPCION QUE DESEAS: ")
    opcion = opcion.upper()

    #menu de opciones para escoger
#     print("\n",opcion)
    if opcion == "A":
        gab1 = ca.union(cb)
        print("\n\tUNION ENTRE A Y B:", gab1)
    elif opcion == "B":
        gab2 = ca.intersection(cb)
        print("\n\tINTERCECCION ENTRE A Y B:", gab2)
    elif opcion == "C":
        gab3 = ca.difference(cb)
        print("\n\tDIFERENCIA ENTRE A Y B:", gab3)
    elif opcion == "D":
        gab4 = ca.issubset(cu)
        print("\n\tEL CONJUNTO A ES SUBCONJUNTO DE UNIVERSO:", gab4)
    elif opcion == "E":
        gab5 = cb.issubset(cu)
        print("\n\tEL CONJUNTO B ES SUBCONJUNTO DE UNIVERSO:", gab5)
    elif opcion == "F":
        gab6 = cu.issuperset(ca)
        print("\n\tEL CONJUNTO UNIVERSO ES SUPERCONJUNTO DEL A:", gab6)
    elif opcion == "G":
        gab7 = ca == cb
        print("\n\tEL CONJUNTO A Y EL B SON IGUALES:", gab7)
    elif opcion == "H":
        gab8 = cu.symmetric_difference(ca)
        print("\n\tDIFERENCIA SIMETRICA DEL UNIVERSO CON CONJUNTO A:", gab8)
    elif opcion == "X":
        print("\n\tNos vemos pronto, gracias por usar el programa")
        loop = False
    else:
        print("\n\tEscribe una opción válida")
        os.system("PAUSE")

    print("\n\t")
    os.system("PAUSE")
    os.system("CLS") #salida del programa