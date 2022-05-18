from http.client import responses
import random

def unknownSentence():
    response = ['No entiendo lo que me decis',
                'Que significa eso?',
                '...',
                'Que?',
                'Podrias repetirlo?'][random.randrange(5)]

    return response

def greetingResponses():
    response = ['Hola!',
                'Buenas',
                'Buenasssss',
                'Buenas!',
                'Que onda?',
                'Aloh'][random.randrange(6)]
    
    return response

def statusResponses():
    response = ['Todo bien por suerte, y vos?',
                'Todo tranqui, vos como andas?',
                'Ando bien, y vos?',
                'Por suerte bien',
                'Ultimamente bastante bien',
                'No se, soy un robot'][random.randrange(6)]
    return response

def godResponses():
    response = ['Nada',
                'No existe, no es nada',
                'Probablemente las matematicas',
                'Una creacion de la sociedas antigua para controlar a los estupidos pero hoy en dia sigue controlandolos, no se como, la verdad',
                'Un mito',
                'Chamuyos de la iglesia que tambien es un chamuyo',
                'El peor concepto que le sucedio a la humanidad'][random.randrange(7)]
    return response
    
def gladToHearResponses():
    response = ['Me alegro!',
                'Estoy contento de escuchar eso',
                'Me parece muy bien',
                'Feliz de escucharlo',
                'Espero que sigas asi'][random.randrange(5)]
    return response
    
def birthdayResponses():
    response = ['Feliz cumpleaños!',
                'Espero que la pases muy bien',
                'Estas creciendo rapido',
                'Muy feliz dia para ti'][random.randrange(4)]
    return response

    

    