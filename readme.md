<p align="center">
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/rock_1faa8.png" width="60"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/roll-of-paper_1f9fb.png" width="60"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/scissors_2702-fe0f.png" width="60"/>
</p>

# Piedra, Papel o Tijera en Python

> Un sencillo juego de terminal hecho en Python. ¡Juega contra la computadora y pon a prueba tu suerte y estrategia!

---

## 🚀 Características

- Juego interactivo en la terminal
- Lógica simple y fácil de entender
- Mensajes claros para el usuario
- Opción para salir en cualquier momento

---

## 🖥️ Requisitos

- Python 3.x

---

## ⚡ Instalación y uso

1. Clona este repositorio o descarga el archivo `piedra_papel_tijera.py`.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el juego con:

```bash
python piedra_papel_tijera.py
```

---

## 🎮 ¿Cómo jugar?

1. Elige entre `piedra`, `papel` o `tijera` cuando se te solicite.
2. La computadora elegirá su jugada al azar.
3. El resultado se mostrará en pantalla.
4. Escribe `salir` para terminar el juego.

---

## 📄 Código principal

```python
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
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el juego, abre un issue o haz un pull request.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
