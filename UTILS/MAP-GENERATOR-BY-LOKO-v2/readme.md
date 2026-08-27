<h1 align="center"> FelipedelosH </h1>
<br>
<h4>LokoMapGenerator</h4>

# Map Generator Utility v2

This is a standalone Python utility designed to convert black-and-white images into binary matrices representing tile-based maps. It is primarily used as a world-building tool for 2D games, such as [LokoMotorGame2](https://github.com/felipedelosh/GamePython).

---

## 📘 Description

The tool reads an image B&W (`map.png`) with resolution (84x48)p * K where:

- **called allways map.png*** the imput file that script read call map.png.
- **K** is a integer number for example 3 = (252x144)p or biger.
- **White pixels** (`#FFFFFF`) represent walkable tiles (1)
- **Black pixels** (`#000000`) represent solid/blocked tiles (0)

The resulting output pieces is a 2D matrix that can be exported as a JSON with propietes:
```
{
    "id": "map_name",
    "collider": [],
    "color": []
}
```
The piece is cut in chunks (84x48)p that reprecen a part of map:

"in chunks"
---

## :hammer:Funtions:

- `Function 1`: Read all map.png in folder INPUT.<br>
- `Function 2`: Verify map.png hav resolution base on (84x48)p.<br>
- `Function 3`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 3a`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 4`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>


## 📦 Project Structure

map-generator/
├── src/
├── main.py 
├── INPUT/
└── requirements.txt 


### 1. Install Dependencies

```
pip install -r requirements.txt
```

## :play_or_pause_button:How to execute a project

run main.py

## :hammer_and_wrench:Tech.

- python
- Pillow
- .gif

## :warning:Warning.

- this software convert a final image... you first paint and then convert.

## Autor

| [<img src="https://avatars.githubusercontent.com/u/38327255?v=4" width=115><br><sub>Andrés Felipe Hernánez</sub>](https://github.com/felipedelosh)|
| :---: |
