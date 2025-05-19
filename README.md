# Turing Machine

A simple implementation of a Turing Machine simulator with Python3, and Pygame visualisation.

## Features

- Simulate Turing Machines with any number of states
- Customisable initial tape conditions
- Step-by-step execution and visualization
- Front-end GUI

## Requirements
There are no requirements for using the `TuringMachine` class. 

For the GUI front-end, `pygame` is required. 

## Front-end Visualisation
To execute the GUI, run `frontend.py` 

Press space to move execute the next step, and press the right arrow key to fast-forward 10 steps. 

![Turing Machine GUI Screenshot](Screenshot.png)

## Class Usage

The class `TuringMachine` can be found in `turing.py`, with the following usage:

```python
from turing import TuringMachine

instruction = [
    # 0      1 
    ['1RB', '1LB'], # Rule A
    ['1LA', '0LC'], # Rule B
    ['---', '1LD'], # Rule C
    ['1RD', '0RA']  # Rule D
] # BB(4) champion instruction; should halt after BB(4)=107 steps
tm = TuringMachine(instruction, initial_tape=[0, 0, 0])

print(repr(tm))
while not tm.done:
    print(repr(tm))
    tm.next_move()

print(repr(tm))
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.