# DiceGame

## Clase Dices

La clase `Dices` modela un par de dados para el juego.

<details>
<summary>Expandir</summary>


### Métodos

#### `__init__(self)`

Inicializa los dados con valores aleatorios entre 1 y 6.

#### `get_dices(self)`

Devuelve los valores actuales de los dados.

#### `rethrow_one(self)`

Vuelve a tirar uno de los dados. Si el primer dado es 4, se vuelve a tirar el segundo dado. De lo contrario, se tira el primer dado nuevamente.

#### `rethrow_both(self)`

Vuelve a tirar ambos dados, asignando nuevos valores aleatorios a cada uno.

</details>

## strats.py

Contiene las funciones que implementan las estrategias de cada jugador.

<details>
<summary>Expandir</summary>

### `points_calculator(dices)`

Calcula y devuelve los puntos obtenidos en una tirada de dados.

- `dices`: Un objeto que representa los dados lanzados.

### `juan_strategy(simulation_sequence=[])`

Implementa la estrategia de Juan para jugar.

- `simulation_sequence`: Una lista opcional. En caso de querer simular la partida, se modificará la lista pasada para registrar las secuencias de tiradas.

### `maria_strategy(juan_points, simulation_sequence=[])`

Implementa la estrategia de María para jugar.

- `juan_points`: Los puntos obtenidos por Juan en su última tirada.
- `simulation_sequence`: Una lista opcional. En caso de querer simular la partida, se modificará la lista pasada para registrar las secuencias de tiradas.

</details>

## simulations.py

Funciones para simular el diálogo de los dos jugadores en una ronda.

<details>
<summary>Expandir</summary>

### `juan_simulation(sequence)`

Imprime en consola la simulación de la secuencia que siguió Juan.

- `sequence`: Secuencia de tiradas de dados de Juan

### `maria_simulation(sequence, juan_points)`

Imprime en consola la simulación de la secuencia que siguió María.

- `sequence`: Secuencia de tiradas de dados de María
- `juan_points`: Puntos de Juan en esa ronda

</details>

## main.py

Funciones que engloban el uso de todas las demás, para simular distintas posibilidades del juego.

<details>
<summary>Expandir</summary>

### Funciones de Juego

Estas funciones facilitan la ejecución y la simulación del juego:

#### `play_one_round()`

Juega una ronda del juego entre Juan y María y devuelve al ganador de la ronda, o None en caso de empate.

#### `play_n_rounds(rounds_amount)`

Juega un número especificado de rondas y devuelve un diccionario que contiene el recuento de victorias de Juan, María y empates.

#### `play_n_matches(rounds, matches)`

Juega un número especificado de partidas, cada una consistiendo de un número especificado de rondas. Devuelve un diccionario que contiene el recuento de victorias de Juan, María y empates en todas las partidas.

#### `simulate_game()`

Simula una ronda entre Juan y María, mostrando su diálogo, registrando las secuencias de tiradas de cada jugador, y devuelve el ganador o empate.

</details>
