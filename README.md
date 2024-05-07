# DiceGame

## Funciones

## Clase `Dices`

La clase `Dices` modela un par de dados para el juego.

### Métodos

#### `__init__(self)`

Inicializa los dados con valores aleatorios entre 1 y 6.

#### `get_dices(self)`

Devuelve los valores actuales de los dados.

#### `rethrow_one(self)`

Vuelve a tirar uno de los dados. Si el primer dado es 4, se vuelve a tirar el segundo dado. De lo contrario, se tira el primer dado nuevamente.

#### `rethrow_both(self)`

Vuelve a tirar ambos dados, asignando nuevos valores aleatorios a cada uno.

## strats.py

### `points_calculator(dices)`

Esta función calcula los puntos obtenidos en una tirada de dados.

- `dices`: Un objeto que representa los dados lanzados.

### `juan_strategy(simulation_sequence=[])`

Implementa la estrategia de Juan para jugar.

- `simulation_sequence`: Una lista opcional donde se registran las secuencias de tiradas simuladas.

### `maria_strategy(juan_points, simulation_sequence=[])`

Implementa la estrategia de María para jugar.

- `juan_points`: Los puntos obtenidos por Juan en su tirada actual.
- `simulation_sequence`: Una lista opcional donde se registran las secuencias de tiradas simuladas.

## simulations.py

### `juan_simulation(sequence)`

Imprime en consola la simulación de la secuencia que siguió Juan.

- `sequence`: Secuencia de tiradas de dados de Juan

### `maria_simulation(sequence, juan_points)`

Imprime en consola la simulación de la secuencia que siguió María.

- `sequence`: Secuencia de tiradas de dados de María
- `juan_points`: Puntos de Juan en esa ronda

