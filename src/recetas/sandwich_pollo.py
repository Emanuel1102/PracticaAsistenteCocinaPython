from src.complementos.pollo import preparar_pollo

def preparar_sandwich(presentacion):
    return {
        'receta': 'sandwich de pollo clasico',
        # llamar presentacion del pollo
        'presentacion': preparar_pollo(presentacion),
        'ingredientes': ['pan de sandwich', 'pechuga de pollo', 'mayonesa', 'lechuga', 'tomate', 'mantequilla'],
        'pasos': ['untar mantequilla en el pan', 'tostar el pan', 'aplicar capa de mayonesa al pan', 'colocar una cama de lechuga', 'colocar rodajas de tomate', 'añadir el pollo', 'cerrar y cortar en diagonal', 'servir con papas fritas o chips']
    }

