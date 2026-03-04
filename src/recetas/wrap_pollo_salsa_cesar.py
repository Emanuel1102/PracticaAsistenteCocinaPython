from src.complementos.pollo import preparar_pollo
from src.complementos.salsa_cesar import preparar_salsa_cesar

def preparar_wrap(presentacion, pimienta):
    return {
    'receta': 'wrap de pollo con salsa cesar',
    # llamar salsa
    'salsa': preparar_salsa_cesar(pimienta),
    # llamar presentacion del pollo
    'presentacion_pollo': preparar_pollo(presentacion),
    'ingredientes': ['tortilla de harina', 'pollo en cubos', 'lechuga picada', 'queso parmesano', 'aderezo cesar', 'crutones triturados'],
    'pasos': ['mezclar en un bol el pollo con la lechuga, queso, crutones y aderezo', 'extender la tortilla caliente sobre una superficie plana', 'colocar el relleno en una linea horizontal cerca del centro', 'doblar los laterales hacia adentro y enrollar con firmeza', 'cortar el wrap por la mitad de forma sesgada y servir de pie para mostrar el relleno']
    }


