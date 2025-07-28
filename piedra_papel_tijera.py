import random

opciones = ['piedra', 'papel', 'tijera']

print('¡Bienvenido a Piedra, Papel o Tijera!')
while True:
    usuario = input('Elige piedra, papel o tijera (o "salir" para terminar): ').strip().lower()
    if usuario == 'salir':
        print('¡Gracias por jugar!')
        break
    if usuario not in opciones:
        print('Opción no válida. Intenta de nuevo.')
        continue
    computadora = random.choice(opciones)
    print(f'La computadora eligió: {computadora}')
    if usuario == computadora:
        print('¡Empate!')
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        print('¡Ganaste!')
    else:
        print('Perdiste :(')
