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

# macOS / Linux (bash, zsh)
source .venv/bin/activate

# macOS / Linux (fish)
source .venv/bin/activate.fish

pip install -r requirements.txt
uvicorn main:app --reload
```

Abrí `http://127.0.0.1:8000/docs` para probar todos los endpoints desde
Swagger UI.

### Alternativa sin activar el entorno

Sirve en cualquier shell y evita problemas de activación:

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn main:app --reload
```

En Windows sería `.venv\Scripts\python -m ...`.

## Solución de problemas

### `source .venv/bin/activate` falla y `uvicorn` no se encuentra

Síntoma típico en **Arch / CachyOS** (o cualquier distro con PEP 668) y/o
al usar **fish**:

```text
.venv/bin/activate (línea 40): 'case' builtin usado fuera de un bloque 'switch'
source: Error al leer el archivo '.venv/bin/activate'
```

Causa: el archivo `.venv/bin/activate` es para **bash/zsh**, no para fish.
Al no activarse el venv, `pip install` usa el Python del sistema (bloqueado
por `externally-managed-environment`) y `uvicorn` nunca queda en el `PATH`.

Solución: usar el script de activación que corresponde a tu shell.

| Shell        | Comando de activación              |
| ------------ | ---------------------------------- |
| bash / zsh   | `source .venv/bin/activate`        |
| fish         | `source .venv/bin/activate.fish`   |
| PowerShell   | `.venv\Scripts\Activate.ps1`       |

Para comprobar que quedó activado, `which python` debe apuntar a
`.../.venv/bin/python` y `which uvicorn` debe existir. Si preferís no
activar nada, usá la [alternativa sin activar el entorno](#alternativa-sin-activar-el-entorno).
