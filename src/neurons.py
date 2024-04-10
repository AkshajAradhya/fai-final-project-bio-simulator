from creature import Creature

class Neuron:
    """Parent data structure for neurons"""

    def __init__(self, creature: Creature, name: str):
        self.connected_to = []  # {neuron that is connected to: weight}
        self.creature = creature  # owner of neurons
        self.name = name
        self.inputs = {}  # {source neuron name: value of input}
        self.output = 0

    def feed_inputs(self):
        """feed output to all connected neurons"""
        for c in self.connected_to:
            c["neuron"].inputs[self.name] = self.output * c["weight"]

    def evaluate(self):
        self.output = 0
    
