import networkx as nx
import logging

logging.basicConfig(level=logging.INFO)


class RateCard:
    def __init__(self, cable_per_meter_verge, cable_per_meter_road, chamber_cost, pot_cost):
        self.cable_per_meter_verge = cable_per_meter_verge
        self.cable_per_meter_road = cable_per_meter_road
        self.chamber_cost = chamber_cost
        self.pot_cost = pot_cost

    def calculate_cost(self, total_length_verge, total_length_road, chamber_count, pot_count):
        """Calculate the total cost based on the rate card and provided data."""
        return (total_length_verge * self.cable_per_meter_verge + total_length_road * self.cable_per_meter_road) + (chamber_count * self.chamber_cost) + (pot_count * self.pot_cost)


def load_graphml(filename):
    """Load graph from a graphml file."""
    try:
        return nx.read_graphml(filename)
    except Exception as e:
        logging.error(f"Error reading the file: {e}")
        return None


def extract_data(graph):
    """Extract relevant data from the graph."""
    if not graph:
        return 0, 0, 0, 0

    total_length_verge = sum(float(data['length']) for _, _, data in graph.edges(data=True) if data.get('material') == 'verge')
    total_length_road = sum(float(data['length']) for _, _, data in graph.edges(data=True) if data.get('material') == 'road')

    chamber_count = sum(1 for _, data in graph.nodes(data=True) if data.get('type') == 'Chamber')
    pot_count = sum(1 for _, data in graph.nodes(data=True) if data.get('type') == 'Pot')

    return total_length_verge, total_length_road, chamber_count, pot_count


def main(filename):
    """Main function to calculate and print the costs."""
    graph = load_graphml(filename)
    total_length_verge, total_length_road, chamber_count, pot_count = extract_data(graph)

    # Assuming rate card costs per meter for road and verge respectively
    rate_card_a = RateCard(cable_per_meter_verge=150, cable_per_meter_road=150, chamber_cost=1000, pot_cost=600)
    rate_card_b = RateCard(cable_per_meter_verge=200, cable_per_meter_road=200, chamber_cost=1200, pot_cost=400)

    cost_a = rate_card_a.calculate_cost(total_length_verge, total_length_road, chamber_count, pot_count)
    cost_b = rate_card_b.calculate_cost(total_length_verge, total_length_road, chamber_count, pot_count)

    logging.info(f"Cost using Rate Card A: £{cost_a}")
    logging.info(f"Cost using Rate Card B: £{cost_b}")


# Test cases
def test_calculate_cost():
    """Test the cost calculation functionality."""
    rate_card_test = RateCard(100, 200, 500, 1000)
    assert rate_card_test.calculate_cost(50, 50, 5, 10) == 27500
    logging.info("Test for calculate_cost passed!")


if __name__ == '__main__':
    file_path = input("Enter the path to the graphml file: ")
    main(file_path)
    test_calculate_cost()
