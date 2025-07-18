# 🎮 GamePython - Motor de Videojuego Modular

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Architecture](https://img.shields.io/badge/Architecture-ECS%20%2F%20State%20Machine-orange)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-brightgreen)

Motor de videojuego 2D en Python con arquitectura modular, máquinas de estado y sistema de componentes.

## 🏗️ Estructura del Proyecto
```bash
src/
├── core/               # Sistemas principales
│   ├── controller.py   # Coordinador global
│   ├── gameStateManager.py  # Máquinas de estado
│   ├── inputHandler.py # Gestión de inputs
│   └── UIManager.py    # Renderizado abstracto
├── entities/           # Entidades del juego
│   ├── player.py       # Lógica del jugador
│   └── world.py        # Gestión del mundo
├── UI/ 
config/ 
├── config.json         # Configuración de controles y estados
assets/
├── images/             # Sprites y fondos
└── LAN/                # Archivos de localización