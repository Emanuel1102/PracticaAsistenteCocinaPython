from src.recetas.ensalada_pollo_cesar import preparar_ensalada_cesar

# Recetas :
# preparar pollo; va en todas
# 
# ensalada cesar con pollo,
# wrap de pollo con salsa cesar
# a parte la salsa; usa tanto para la ensalada como para el wrap
# 
# sandwich clasico de pollo,



# resultado esperado (ejemplo):
# {
    # plato escogido
    # "receta": ”sandwich”,
    #
    # presentacion de la salsa (diccionario)
    # "salsa": {
    #
        # “pimienta_negra” : True/False,
        #
        # “sal” : “al gusto”,
        #
        # “zumo_limon” : “10 ml”
        #
    # },
    #
    # presentacion del pollo
    # “presentacion_pollo” : “normal”,   
    #
    # los ingresientes y pasos son propios de cada plato, asi como el nombre del plato escogido
    # "ingredientes": ["pan de sándwich", "queso", "lechuga", "tomate"],
    #
    # "pasos": ["Tostar ligeramente el pan", "Colocar el pollo”, “Colocar queso”, “agregar salsa" ]
    #
# }


ensalada_pollo_cesar=1
wrap_pollo_salsa_cesar=2
sandwich_pollo=3

plato=int(input('''¿Que plato desea ordenar? (indique con el numero de la opcion):
            1. Ensalada César con pollo
            2. Wrap de pollo con salsa César
            3. Sándwich clásico de pollo 

            => '''))

plato_escogido=''

if plato==ensalada_pollo_cesar:
    plato_escogido = preparar_ensalada_cesar()
elif plato==wrap_pollo_salsa_cesar:
    print('wrap')
elif plato==sandwich_pollo:
    print('sandwich')
else:
    print('No se reconoce tu respuesta')


print(plato_escogido)






# 1. Ensalada César con pollo

# 2. Wrap de pollo con salsa César

# 3. Sándwich clásico de pollo


#  pasos e ingredientes para cada plato:
# 1. Sándwich de Pollo Clásico
# Ingredientes: Pan (molde o brioche), pechuga de pollo, mayonesa, lechuga, tomate, mantequilla.
# Paso a paso para emplatar:
# Unta mantequilla en el pan y tuéstalo hasta que dore.
# Aplica una capa de mayonesa en ambas tapas.
# Coloca una cama de lechuga y encima rodajas de tomate.
# Añade el pollo (filete o mezcla desmenuzada).
# Cierra, corta en diagonal y sirve con papas fritas o chips.

# 2. Ensalada César con Pollo
# Ingredientes: Lechuga romana, pechuga de pollo a la plancha, queso parmesano, crutones, aderezo César.
# Paso a paso para emplatar:
# Mezcla la lechuga seca con el aderezo en un bol hasta cubrirla bien.
# Pasa la lechuga al plato o ensaladera de servicio.
# Distribuye el pollo en tiras sobre la lechuga.
# Esparce los crutones de forma uniforme.
# Termina con lascas o lluvia de queso parmesano por encima.
# 3. Wrap de Pollo César

# Ingredientes: Tortilla de harina grande, pollo en cubos, lechuga picada, queso parmesano, aderezo César, crutones triturados.
# Paso a paso para emplatar:
# Mezcla en un bol el pollo, lechuga, queso, crutones y aderezo.
# Extiende la tortilla caliente sobre una superficie plana.
# Coloca el relleno en una línea horizontal cerca del centro.
# Dobla los laterales hacia adentro y enrolla con firmeza.
# Corta el wrap por la mitad de forma sesgada y sírvelo de pie para mostrar el relleno.