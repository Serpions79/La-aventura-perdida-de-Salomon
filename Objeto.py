class Objeto:
    ataque=0
    defensa=0
    resistencia=0
    def __init__(self,nombre,ataque,defensa,resistencia,valor):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.resistencia = resistencia
        self.valor = valor
Monedero=Objeto("Monedero",0,0,0,11)
Objetos=[Monedero]
def buscarObjeto(nombre):
    encontrado=0
    i=0
    while i<len(Objetos) and encontrado==0:
        if Objetos[i].nombre ==nombre:
            encontrado=1
        else:
            i=i+1
    if encontrado==1:
        return 1
    else:
        return 0
print("Bienvenido a caminos distintos donde tendras que escoger tu propio camino segun que opciones escogas")
print("Empezaremos con algo sencillo ")
print("Elige 1 o 2 ")
Algo=int(input())
if Algo==1:
    print("Has escogido el numero 1 apareceras en una selva" )
elif Algo==2:
     print("Has escogido el numero 2 apareceras en un desierto")
print("Vaya has aparecido en este bioma peculiar ten te puedo dar 3 objetos pero solo puedes escoger 1 para sobrevivir ")
print("Si quieres una cuerda escoge 1 si quieres una bengala escoge 2 si quieres un machete escoge 3")
Object=int(input())
if  Object==1:
    print("Has escogido la cuerda buena eleccion ")
    Objetos.append(Objeto("Cuerda",5,6,6,6))
elif Object==2:
     print("Has escogido la bengala magnifica idea ") 
     Objetos.append(Objeto("Bengala",2,7,8,7))
elif Object==3:
     print("Has escogido el machete, si te soy sincero yo tambien lo habria escogido ")
     Objetos.append(Objeto("Machete",8,6,4,5))
print("Ahora que ya estamos listos vamonos")
print("4 HORAS DESPUES")
print("Ya se esta haciendo de noche. Vaya mira lo que veo es una cabanya de madera a tu derecha pero veo una cueva tambien a tu izquierda ")
print("Escoge 1 para pasar la noche en la cabanya o escoge 2 para pasar la noche en la cueva")
Refugio=int(input())
if Refugio==1:
   print("Has escogido la cabanya me parece correcto ")
elif Refugio==2:
     print("Has escogido la cueva buena eleccion ")
print("HAS PASADO LA 1r NOCHE FIN DE LA PARTIDA")
print("SI TE QUEDASTE CON GANAS DE MAS PODRAS JUGAR LA SEGUNDA PARTE DENTRO DE 1 ANYO")
print("INSERTAR MUSICA DE VIDEOJUEGOS")
print("Oh vaya estas aqui aun")
print("Bueno te dejo jugar la segunda parte")
print("MUSICA DE ACCION")
print("Oh no te estan persiguiendo unos lobos salvajes y es de noche")
if buscarObjeto("Bengala")==1:
    print("Teniendo la bengala puedes utilizarla, Quieres utilizarla ahora? 1 si 2 no") 
    Hola=int(input())
    if Hola==1:
       print("Has utilizado la bengala y los lobos se han ido")
    elif Hola==2:
        print("Los lobos te han dejado a media vida pero se han ido")
print("Ya llevas 3 horas y aun no has comido pero mira lo que veo es un ciervo")
if buscarObjeto("Machete")==1:
    print("Puedes utilizar el machete para comer el ciervo (1) o puedes seguir caminando y buscar otra comida (2)")
    A=int(input())
    if A==1:
        print("Has utilizado el Machete... pero el ciervo a escapado")
    elif A==2:
        print("Bien hecho, como podrias matar a un ciervo tu solo con un machete?")
print("Mira has encontrado otra casa abandonada")
print("Quieres ir a investigar esa casa?")
print("1 SI 2 NO")
SIUUU=int(input())
if SIUUU==1:
    print("Has entrado a la casa y mira habia un monton de comida toda esta comida nos bastara para 1 semana")
elif SIUUU==2:
    print("Mejor no entraremos a esa casa pero parece oler bastante bien seguro que no quieres entrar a la casa? Pon 1 si al final quieres ir o pon 2 si no quieres ir")
    B=int(input())
    if B==1:
        print("Has entrado a la casa y mira habia un monton de comida toda esta comida nos bastara para 1 semana")
    elif B==2:
        print("Ok no iremos a la casa abandonada")



