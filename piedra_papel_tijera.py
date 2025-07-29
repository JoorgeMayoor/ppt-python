import random

opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']

# Diccionario con las reglas del juego: cada opción vence a las opciones en su lista
reglas = {
    'piedra': ['tijera', 'lagarto'],      # Piedra aplasta tijera y aplasta lagarto
    'papel': ['piedra', 'spock'],         # Papel cubre piedra y desautoriza a Spock
    'tijera': ['papel', 'lagarto'],       # Tijera corta papel y decapita lagarto
    'lagarto': ['papel', 'spock'],        # Lagarto come papel y envenena a Spock
    'spock': ['piedra', 'tijera']         # Spock vaporiza piedra y rompe tijera
}

print('¡Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!')
print('Reglas:')
print('- Tijera corta Papel y decapita Lagarto')
print('- Papel cubre Piedra y desautoriza a Spock')
print('- Piedra aplasta Lagarto y aplasta Tijera')
print('- Lagarto envenena a Spock y come Papel')
print('- Spock vaporiza Piedra y rompe Tijera')

while True:
    usuario = input('Elige piedra, papel, tijera, lagarto o spock (o "salir" para terminar): ').strip().lower()
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
    elif computadora in reglas[usuario]:
        print('¡Ganaste!')
    else:
        print('Perdiste :(')
