# A Collection of Mathematical Visualisations

These visualations are created using the matplotlib.animation library.

At the moment the main contents of this repository is cellular automata, as they provide interesting visualiations.



## Lissajouse curves.

Shows the superposition of two sine waves which are perpendicular to each other. By changing the ratio between the angular frequencies of the two waves, the illusion of a three dimensional shape is created.

![Lissajouse curve gif](./anims/lissajous.gif)

## Rose (Rhodonea) curves.
Sinusoidal patterns that create the shapes of roses, they can be specified by a number of a number of polar equations, these were created using the basic equation $r = a cos(k\theta)$. The shape of the rose is dependant on the angular frequency $k = \frac{n}{d}$.

![Rose curve gif](./anims/rose.gif)


## Conways game of life.

Cells can be in one of two states, alive or dead. The state in which the cell is in is dependdant on the number of neighbours around the cell.

[Game of life wiki page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life?useskin=vector)


![Conways game of life animation](./anims/game_of_life.gif)


## Wolfram codes.

A 1-D cellular automata that can create interesting patterns if each frame is layered under the last. There are 255 total wolfram codes however many of them are chiral. Here are just a couple of my favourites :)


![Wolfram code 99](./anims/wolframcode99.gif)

![Wolfram code 105](./anims/wolframcode105.gif)


## Langtons ant

An ant moves a unit forward, if the square below it is a 1, the ant turns 90 degreees clockwise and the square becomes a zero. If the square below it is a 0 the ant turns 90 degrees anti-clockwise and the square bedomes a 1. 


![A collection of langtons ants](./anims/ants.gif)
