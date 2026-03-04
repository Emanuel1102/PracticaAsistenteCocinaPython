from src.complementos.pollo import preparar_pollo
from src.complementos.salsa_cesar import preparar_salsa_cesar


def preparar_ensalada_cesar(presentacion, pimienta):
    return {
        'receta': 'Ensalada cesar',
        # llamar salsa
        'salsa': preparar_salsa_cesar(pimienta),
        # llamar presentacion del pollo
        'presentacion_pollo': preparar_pollo(presentacion),
        'ingredientes':['lechuga romana', 'pechuga de pollo a la plancha', 'queso parmesano', 'crutones', 'aderezo cesar'],
        'pasos':['mezclar la lechuga seca con el aderezo en un bol hasta cubrirla bien', 'pasar la lechuga al plato', 'destribuir el pollo sobre la lechuga', 'exparcir los crutones de forma uniforme', 'lluvia de queso parmesano por encima']
    }

