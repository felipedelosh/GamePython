# 🎮 GamePython - Motor de Videojuego Modular

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Architecture](https://img.shields.io/badge/Architecture-ECS%20%2F%20State%20Machine-orange)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-brightgreen)

Motor de videojuego 2D en Python con arquitectura modular, máquinas de estado y sistema de componentes.

## 🏗️ Estructura del Proyecto
```
my_game_project/
├── assets/          
│   ├── images/
│   ├── sounds/
│   ├── music/
│   └── fonts/
│
├── config/ 
│
├── Docs/
│
├── src/                   
│   ├── core/              
│   ├── entities/          
│   ├── levels/            
│   ├── UI/                
│   |── systems/           
│
│
├── UTILS/
│   ├── MapGenerator/
│
├── data/                 
│
├── tests/                 
│                
├── .gitignore 
├── main.py 
├── readme.md             
└── requirements.txt      
```

# 📌 Configuración del Juego (`config.json`)

Este archivo define los parámetros principales de **LokoMotorGame2**.  
Asegúrate de revisarlo antes de ejecutar el juego para personalizar la experiencia.

| **Clave**              | **Valor por defecto**       | **Descripción**                                                                 |
|-------------------------|-----------------------------|---------------------------------------------------------------------------------|
| `displayW`             | 640                         | Ancho de la ventana del juego en píxeles.                                       |
| `displayH`             | 480                         | Alto de la ventana del juego en píxeles.                                        |
| `floorW`               | 84                          | Ancho del mapa del mundo (en tiles).                                            |
| `floorH`               | 48                          | Alto del mapa del mundo (en tiles).                                             |
| `LAN`                  | "ESP"                       | Idioma del juego (`ESP`, `ENG`, etc.).                                          |
| `FPS`                  | 32                          | Frames por segundo que intenta renderizar el juego.                             |
| `intro_duration`       | 1500                        | Duración de la pantalla de introducción (milisegundos).                         |
| `env`                  | "dev"                       | Entorno de ejecución: `"dev"` (desarrollo) o `"prod"` (producción).             |
| `logging`              | true                        | Activa (`true`) o desactiva (`false`) el sistema de logs centralizado.          |
| `playerName`           | "Human"                     | Nombre por defecto del jugador.                                                 |
| `playerAge`            | 0                           | Edad inicial del jugador.                                                       |
| `playerVelocity`       | 5                           | Velocidad de movimiento del jugador (píxeles por frame).                        |
| `player_look_up`       | "player_look_up.png"        | Sprite del jugador mirando hacia arriba.                                        |
| `player_look_left`     | "player_look_left.png"      | Sprite del jugador mirando hacia la izquierda.                                  |
| `player_look_right`    | "player_look_right.png"     | Sprite del jugador mirando hacia la derecha.                                    |
| `player_look_down`     | "player_look_down.png"      | Sprite del jugador mirando hacia abajo.                                         |
| `player_w`             | 50                          | Ancho del sprite del jugador en píxeles.                                        |
| `player_h`             | 100                         | Alto del sprite del jugador en píxeles.                                         |
| `key_UP`               | 38                          | Tecla para moverse hacia arriba (código de tecla).                              |
| `key_RIGTH`            | 39                          | Tecla para moverse hacia la derecha (código de tecla).                          |
| `key_DOWN`             | 40                          | Tecla para moverse hacia abajo (código de tecla).                               |
| `key_LEFT`             | 37                          | Tecla para moverse hacia la izquierda (código de tecla).                        |
| `key_SELECT`           | 32                          | Tecla de selección (por defecto: barra espaciadora).                            |
| `key_START`            | 13                          | Tecla de inicio/pausa (por defecto: Enter).                                     |
| `key_B`                | 90                          | Tecla de acción B (por defecto: Z).                                             |
| `key_A`                | 88                          | Tecla de acción A (por defecto: X).                                             |
| `key_Y`                | 67                          | Tecla de acción Y (por defecto: C).                                             |
| `key_X`                | 86                          | Tecla de acción X (por defecto: V).                                             |
| `key_L`                | 65                          | Tecla de acción L (por defecto: A).                                             |
| `key_R`                | 83                          | Tecla de acción R (por defecto: S).                                             |
| `statesMachines.game.initial`     | "intro"         | Estado inicial de la máquina de estados del juego.                              |
| `statesMachines.game.states`      | ["intro","mainMenu","gameStart","gamePause","gameOptions"] | Lista de estados del juego.                  |
| `statesMachines.game.conections`  | [ ... ]         | Reglas de transición entre estados del juego.                                   |
| `statesMachines.mainMenu.initial` | "newGame"       | Estado inicial del menú principal.                                              |
| `statesMachines.mainMenu.states`  | ["newGame","continueGame","optionsGame","exitGame"] | Lista de opciones del menú principal.        |
| `statesMachines.mainMenu.conections` | [ ... ]      | Reglas de transición entre opciones del menú principal.                         |

---

# 📌 SYSTEMS

## ECS

El sistema ECS (Entity–Component–System) se implementa en el motor de juego para mejorar la escalabilidad, la organización del código y la reutilización de lógicas.
Permite separar claramente:

Entidades (Entity) → Son identificadores o contenedores.
Componentes (Component) → Contienen datos (sin lógica).
Sistemas (System) → Ejecutan la lógica sobre entidades con ciertos componentes.

Esto garantiza un motor de juego más modular y mantenible.

## 🏗️ Estructura del ECS

src/ecs/component.py
Define los componentes principales usados por el Player


```
src/
 └── ecs/
      ├── __init__.py
      ├── component.py         # Clase base Component
      ├── components.py        # Definiciones de componentes concretos
      ├── entity.py            # Clase base Entity
      ├── system.py            # Clase base System
      ├── systems/             # (Carpeta) Sistemas concretos
      │    ├── __init__.py
      │    ├── movementSystem.py
      │    ├── renderSystem.py
      │    └── collisionSystem.py
      ├── manager/             # (Carpeta) Gestores ECS
      │    ├── __init__.py
      │    ├── entityManager.py
      │    └── systemManager.py
      └── utils.py             # Utilidades opcionales (ej. factories)
```



## MovementSystem

El **MovementSystem** centraliza la lógica de movimiento de todas las entidades que poseen los componentes necesarios.  
De esta forma, el desplazamiento ya no depende de métodos internos de `Player`, sino de un sistema independiente que procesa las entradas del jugador (y futuras IA).

```
src/systems/movementSystem.py
```

## 🧱 CollisionSystem

El CollisionSystem es el responsable de evitar que las entidades atraviesen los límites del mundo o entren en zonas no caminables definidas en el mapa JSON.
Funciona en conjunto con el MovementSystem, que calcula el desplazamiento según la entrada del jugador.

El `CollisionSystem` se apoya en un mapa de colisiones (`self.world.collider`) donde:

- `0` representa una celda caminable.
- `1` representa una celda bloqueada.

## Como agregar un nuevo sistema

El motor implementa la arquitectura ECS (Entity–Component–System).
Para añadir un nuevo sistema (por ejemplo: CollisionSystem, HealthSystem, RenderSystem), se deben seguir los siguientes pasos:

1. Crear el Archivo del Sistema
Dentro de la carpeta src/systems/, crea un archivo con el nombre del sistema.

2. Crear el componente
Si tu sistema requiere nuevos datos, crea un componente en src/ecs/components.py.

3. Definir la Clase del Sistema
Todos los sistemas heredan de System (definida en src/ecs/system.py).
```
from src.ecs.system import System
from src.ecs.components import XComponent

class XSystem(System):
    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(XComponent):
                x = entity.get_component(XComponent)
                  ...
```

4. Registrar el Sistema en el Controlador
```
from src.systems.XSystem import XSystem

self.systems = [
    MovementSystem(...),
    CollisionSystem(...),
    XSystem()  # <-- nuevo sistema
]
```

5. Integrar con Entidades
```
from src.ecs.components import XComponent

self.add_component(XComponent(100))
```

6. Validar la Ejecución
Al ejecutar el juego, el sistema se actualizará automáticamente en cada frame, siempre que esté registrado en self.systems.

