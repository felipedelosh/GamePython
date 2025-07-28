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