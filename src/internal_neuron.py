from neurons import Neuron
import math

class InternalNeuron(Neuron):
    def evaluate(self):
        """Calulate the output for the the internal neuron"""
        self.output = math.tanh(sum(self.inputs.values()))
