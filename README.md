# Gigaclear Cost Calculator

This program calculates the cost of setting up a network based on the given specifications and rate cards. Gigaclear focuses on putting cables in the ground, connecting pots to a central cabinet via cables buried in trenches and chambers. The cost of setting up the network is based on predefined rate cards.

## Prerequisites

- Python 3.x
- NetworkX library (for handling and processing graphs)

To install NetworkX:
```bash
pip install networkx
```

## Usage

1. Navigate to the `src` directory:
```bash
cd path/to/src
```

2. Run the program:
```bash
python3 gigaclear_calculator.py
```

3. You'll be prompted to enter the path to the `.graphml` file containing the network specifications. Provide the relative or absolute path to the file:
```bash
Enter the path to the graphml file: ../data/problem.graphml
```

4. The program will display the calculated cost for the network setup based on the two rate cards.

## Functionality

1. **RateCard Class**: This class represents a rate card and has methods to calculate costs based on the given parameters.
2. **load_graphml Function**: Reads a `.graphml` file and returns a graph.
3. **extract_data Function**: Extracts necessary data from the graph, such as total cable lengths, number of chambers, and pots.
4. **main Function**: Main driver function that integrates the above functions and calculates costs.

## Testing

The program includes a basic test to ensure the `calculate_cost` method works correctly. More tests can be added to validate other functionalities and edge cases.

## Future Improvements

1. Handling of more edge cases, e.g., missing attributes in the `.graphml` file.
2. Support for more file formats beyond `.graphml`.
3. A more interactive UI/CLI for enhanced user experience.
4. Expansion of test cases for robust validation.
