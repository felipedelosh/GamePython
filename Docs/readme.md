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

## 📌 Configuración del Juego (`config.json`)

| **Clave**            | **Valor por defecto**         | **Descripción**                                                                 |
|-----------------------|------------------------------|---------------------------------------------------------------------------------|
| `displayW`            | 640                          | Ancho de la ventana del juego en píxeles.                                       |
| `displayH`            | 480                          | Alto de la ventana del juego en píxeles.                                        |
| `floorW`              | 84                           | Ancho del mapa del mundo (tiles o celdas).                                      |
| `floorH`              | 48                           | Alto del mapa del mundo (tiles o celdas).                                       |
| `LAN`                 | "ESP"                        | Idioma de la interfaz (`ESP`, `ENG`, etc.).                                     |
| `FPS`                 | 32                           | Frames por segundo que intentará renderizar el juego.                           |
| `intro_duration`      | 1500                         | Duración de la pantalla de introducción (ms).                                   |
| `env`                 | "dev"                        | Entorno de ejecución: `"dev"` (desarrollo) o `"prod"` (producción).             |
| `logging.enabled`     | true                         | Activa o desactiva el sistema de logs centralizado.                             |
| `logging.level`       | "DEBUG"                      | Nivel de logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`).                         |
| `logging.file`        | "logs/game.log"              | Ruta del archivo donde se guardarán los logs.                                   |
| `playerName`          | "Human"                      | Nombre por defecto del jugador.                                                 |
| `playerAge`           | 0                            | Edad inicial del jugador.                                                       |
| `playerVelocity`      | 5                            | Velocidad de movimiento del jugador (píxeles por frame).                        |
| `player_look_up`      | "player_look_up.png"         | Sprite del jugador mirando hacia arriba.                                        |
| `player_look_left`    | "player_look_left.png"       | Sprite del jugador mirando hacia la izquierda.                                  |
| `player_look_right`   | "player_look_right.png"      | Sprite del jugador mirando hacia la derecha.                                    |
| `player_look_down`    | "player_look_down.png"       | Sprite del jugador mirando hacia abajo.                                         |
| `player_w`            | 50                           | Ancho del sprite del jugador.                                                   |
| `player_h`            | 100                          | Alto del sprite del jugador.                                                    |
| `key_UP`              | 38                           | Tecla para moverse hacia arriba (código de tecla).                              |
| `key_RIGTH`           | 39                           | Tecla para moverse hacia la derecha (código de tecla).                          |
| `key_DOWN`            | 40                           | Tecla para moverse hacia abajo (código de tecla).                               |
| `key_LEFT`            | 37                           | Tecla para moverse hacia la izquierda (código de tecla).                        |
| `key_SELECT`          | 32                           | Tecla de selección (por defecto: barra espaciadora).                            |
| `key_START`           | 13                           | Tecla de inicio/pausa (por defecto: Enter).                                     |
| `key_B`               | 90                           | Tecla de acción B (por defecto: Z).                                             |
| `key_A`               | 88                           | Tecla de acción A (por defecto: X).                                             |
| `key_Y`               | 67                           | Tecla de acción Y (por defecto: C).                                             |
| `key_X`              | 86                           | Tecla de acción X (por defecto: V).                                             |
| `key_L`               | 65                           | Tecla de acción L (por defecto: A).                                             |
| `key_R`               | 83                           | Tecla de acción R (por defecto: S).                                             |
| `statesMachines.game.initial` | "intro"             | Estado inicial de la máquina de estados del juego.                              |
| `statesMachines.game.states`  | ["intro","mainMenu","gameStart","gamePause","gameOptions"] | Lista de estados disponibles en el juego.        |
| `statesMachines.game.conections` | [ ... ]          | Conexiones entre estados del juego según eventos o controles.                   |
| `statesMachines.mainMenu.initial` | "newGame"       | Estado inicial del menú principal.                                              |
| `statesMachines.mainMenu.states` | ["newGame","continueGame","optionsGame","exitGame"] | Lista de opciones del menú principal.        |
| `statesMachines.mainMenu.conections` | [ ... ]      | Conexiones entre opciones del menú principal según entradas de usuario.         |


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