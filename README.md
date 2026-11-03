# TP1 — ABM de Usuarios + ABM de Videojuegos (FastAPI)

API con **FastAPI** + **Pydantic** que implementa el ABM (Alta, Baja,
Modificación) completo de la entidad `Usuario` y de la entidad `Videojuego`,
con almacenamiento en memoria.

- Documentación interactiva (Swagger): **`http://127.0.0.1:8000/docs`**

## Endpoints usuarios

| Método | Ruta                | Descripción                                                        |
| ------ | ------------------- | ------------------------------------------------------------------ |
| GET    | `/user`             | Lista todos los usuarios                                           |
| GET    | `/user?is_active=`  | Filtra por estado: `true` activos, `false` inactivos (sin param: todos) |
| POST   | `/user`             | Alta de usuario                                                    |
| PUT    | `/user/{id}`        | Modifica nombre y/o estado; devuelve el usuario actualizado        |
| DELETE | `/user/{id}`        | Baja de usuario                                                    |

Todos los casos de usuario inexistente responden `404`.

## Endpoints videojuegos

Entidad con 5 campos: `id`, `titulo`, `desarrollador`, `anio` y
`esta_disponible`.

| Método | Ruta                        | Descripción                                                        |
| ------ | --------------------------- | ------------------------------------------------------------------ |
| GET    | `/videojuego`               | Lista todos los videojuegos                                        |
| GET    | `/videojuego?esta_disponible=` | Filtra por disponibilidad (sin param: todos)                     |
| GET    | `/videojuego/{id}`          | Consulta por id                                                    |
| POST   | `/videojuego`               | Alta de videojuego                                                 |
| PUT    | `/videojuego/{id}`          | Modifica campos (los que se envíen); devuelve el videojuego actualizado |
| DELETE | `/videojuego/{id}`          | Baja de videojuego                                                 |

Videojuego inexistente responde `404`.

## Cómo levantar la aplicación

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Abrí `http://127.0.0.1:8000/docs` para probar todos los endpoints desde
Swagger UI.
