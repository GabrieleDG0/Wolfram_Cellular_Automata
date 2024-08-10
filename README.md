# Wolfram Cellular Automaton

## Introduction
Wolfram Cellular Automaton is a class of one-dimensional cellular automata developed by mathematician Stephen Wolfram. These automata are defined by a set of simple rules that determine the state of each cell based on its current state and the state of its immediate neighbors. In this implementation, users can enter a rule number (0-255) to observe different patterns and behaviors.

**You can find a .exe file, inside the .rar file, if you want to try the project, without needing to install Python, if you have a Windows system.**

## Rules
The automaton works with a grid of cells, each of which can assume one of two states: alive (1) or dead (0). The state of each cell in the next generation is determined by the rule number specified by the user. The rule number is converted into an 8-bit binary number that defines the next state of a cell based on its current state and the states of its left and right neighbors.

Rule 30, for example, is represented as 00011110 in binary numbers:

- 000 -> **0**
- 001 -> **1**
- 010 -> **1**
- 011 -> **1**
- 100 -> **1**
- 101 -> **0**
- 110 -> **0**
- 111 -> **0**

***Overview of the implementation***

This implementation of the Wolfram Cellular Automaton was created using Pygame, a popular library for creating games and multimedia applications in Python.

## Setup and initialization
1) Initialization of Pygame: The Pygame library is initialized to process graphics and events.
2) Color definitions: The colors for the cells and grid lines are defined.
3) Screen and grid dimensions: The dimensions of the screen and the size of the grid are defined to create the game field.

#### Drawing the grid
Drawing the grid: Functions are provided for drawing the grid lines and cells on the screen. Live cells are drawn as filled squares.

#### Game logic
Update cells: Functions are provided to calculate the next state of the grid based on the current configuration of live and dead cells. This includes checking neighboring cells and applying the rules defined by the rule number specified by the user.

## User interaction
Run the Python file and use the following commands:

- Input box: enter the rule number (0-255) to see different behaviors of the automaton.
- Keyboard control:
  - Enter: Starts the simulation with the rule number entered.
  - R key: Resets the simulation and allows you to enter a new rule number.

#### Main loop
Game loop: The main loop of the program controls the frame rate, checks for user input, updates the cell states and redraws the grid.

## Applications and simulations
The Wolfram Cellular Automaton, while simple, has profound implications and applications in various fields:

- Cellular automata are suitable for representing and simulating the global evolution of phenomena that depend only on local laws. Examples of such phenomena are the physical behavior of perfect gasses, the evolution of a population, an ecosystem (e.g. Wa-gate), the movement of DNA strands in a solution.
- Cellular automata are usually very elegant to describe patterns that occur in nature: from the stripes of a zebra to the spotted coat of a cheetah to the stripes of desert dunes. Another example is some marine molluscs, such as those of the genus Conus, whose coloration is produced by natural cellular automata.
- Cellular automata are effectively used for the production of ring tones. A whole web portal (tungsten tones) shows how a sequence of steps of a cellular automaton can be converted into musical notes using certain rules and thus generate music.

## Classification
In A New Kind of Science and a series of other publications dating back to the mid-1980s, Stephen Wolfram defined four classes into which every cellular automaton and some other simple computational models can be divided based on their behaviour.

- Class 1: Almost all initial patterns evolve rapidly to stable, homogeneous states. Any randomness in the initial patterns disappears.
- Class 2: Almost all initial patterns quickly develop into stable or oscillating structures. The randomness of the initial patterns can be ignored, but is present in some.
- Class 3: Almost all initial patterns develop in a pseudo-random or chaotic manner. Any stable structure appears to be quickly destroyed by the surrounding noise.
- Class 4: Almost all initial patterns develop into structures that interact in complex and interesting ways. Class 2: Stable or oscillating structures may be the end result, but the number of steps required to reach this state can be large, even if the initial pattern is relatively simple.

## Contributions
- Official site for research on Wolfram Cellular Automata: https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
- Wikipedia, if you want to learn more: https://en.wikipedia.org/wiki/Cellular_automaton
- A new kind of science (by *Stephen Wolfram*): https://www.wolframscience.com/nks/

Thanks and credit to the Wolfram Cellular Automata official site for the rules images.
