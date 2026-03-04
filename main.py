from src.recetas.ensalada_pollo_cesar import preparar_ensalada_cesar
from src.recetas.wrap_pollo_salsa_cesar import preparar_wrap
from src.recetas.sandwich_pollo import preparar_sandwich

ensalada_pollo_cesar=1
wrap_pollo_salsa_cesar=2
sandwich_pollo=3

plato=int(input('''¿Que plato desea ordenar? (indique con el numero de la opcion):
            1. Ensalada César con pollo
            2. Wrap de pollo con salsa César
            3. Sándwich clásico de pollo 

            => '''))

plato_escogido=''

presentacion_pollo=input('¿En que presentacion desea el pollo? , nuestras presentaciones son "tiras" o "normal"; escriba alguna de las dos opciones => ')

pimienta_en_salsa=False
pimienta=input('¿Desea pimienta negra molida en su salsa?, si es asi escriba "si", de lo contrario ignore presionando enter => ')

if pimienta=='si':
    pimienta_en_salsa=True

if presentacion_pollo=='tiras' or presentacion_pollo=='normal':
    if plato==ensalada_pollo_cesar:
        plato_escogido = preparar_ensalada_cesar(presentacion_pollo, pimienta_en_salsa)
    elif plato==wrap_pollo_salsa_cesar:
        plato_escogido=preparar_wrap(presentacion_pollo, pimienta_en_salsa)
    elif plato==sandwich_pollo:
        plato_escogido=preparar_sandwich(presentacion_pollo)
    else:
        print('No se reconoce tu respuesta')

    print(plato_escogido)
else:
    print('Solamente manejamos el pollo en tiras o normal')
