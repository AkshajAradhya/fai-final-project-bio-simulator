from neurons import Neuron

class ActionNeuron(Neuron):
    def evaluate(self):
        """Calulate the output for the the action neuron (raw sum)"""
        self.output = sum(self.inputs.values())