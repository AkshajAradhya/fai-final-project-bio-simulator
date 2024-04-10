from neurons import Neuron
import math
import random
import constants
import utils

class SensoryNeuron(Neuron):
    def evaluate(self):
        """Calulate the output for the sensor neuron"""
        match self.name:
            case "LOC_X":
                # location on the x axis
                self.output = self.creature.x / constants.WORLD_WIDTH
            case "LOC_Y":
                # location on the y axis
                self.output = self.creature.y / constants.WORLD_HEIGHT
            case "BOUNDARY_DIST_X":
                # Distance to the nearest boundary on the x axis
                self.output = min(
                    self.creature.x, constants.WORLD_WIDTH - self.creature.x - 1
                ) / int(constants.WORLD_WIDTH / 2 - 1)
            case "BOUNDARY_DIST_Y":
                # Distance to the nearest boundary on the x axis
                self.output = min(
                    self.creature.y, constants.WORLD_HEIGHT - self.creature.y - 1
                ) / int(constants.WORLD_HEIGHT / 2 - 1)
            case "BOUNDARY_DIST":
                # Distance to the nearest boundary
                self.output = (
                    2
                    * min(
                        self.creature.x,
                        constants.WORLD_WIDTH - self.creature.x - 1,
                        self.creature.y,
                        constants.WORLD_HEIGHT - self.creature.y - 1,
                    )
                    / int(max(constants.WORLD_WIDTH / 2 - 1, constants.WORLD_HEIGHT / 2 - 1))
                )
            case "GENETIC_SIM_FWD":
                # How genetically similar the creature directly forward is
                # (return 0 if noo one's there)
                tx, ty = (
                    self.creature.x + self.creature.facing_x,
                    self.creature.y + self.creature.facing_y,
                )
                from creature import Creature
                if utils.is_in_world(tx, ty) and type(constants.WORLD[ty][tx]) == Creature:
                    # returns how many bits are different, scaled to (0, 1)
                    g1 = "".join(
                        [
                            bin(int(gene, 16))[2:].zfill(24)
                            for gene in self.creature.genome.split(" ")
                        ]
                    )
                    g2 = "".join(
                        [
                            bin(int(gene, 16))[2:].zfill(24)
                            for gene in constants.WORLD[ty][tx].genome.split(" ")
                        ]
                    )

                    N = 0
                    L = len(g1)
                    for i in range(L):
                        if g1[i] != g2[i]:
                            N += 1
                    self.output = 1 - min(1, (2 * N) / L)
            case "LAST_MOVE_DIR_X":
                # Direction on the x axis
                self.output = (self.creature.facing_x + 1) / 2
            case "LAST_MOVE_DIR_Y":
                # Direction on the y axis
                self.output = (self.creature.facing_y + 1) / 2
            case "LONGPROBE_POP_FWD":
                # How far away a creature is in the forward direction
                for d in range(1, constants.LONG_PROBE_DISTANCE):
                    tx = self.creature.x + d * self.creature.facing_x
                    ty = self.creature.y + d * self.creature.facing_y
                    from creature import Creature
                    if utils.is_in_world(tx, ty) and type(constants.WORLD[ty][tx]) == Creature:
                        self.output = (
                            constants.LONG_PROBE_DISTANCE - d + 1
                        ) / constants.LONG_PROBE_DISTANCE
                        break
                self.output = 0
            case "LONGPROBE_BAR_FWD":
                # How far away a barrier is in the forward direction
                for d in range(1, constants.LONG_PROBE_DISTANCE):
                    tx = self.creature.x + d * self.creature.facing_x
                    ty = self.creature.y + d * self.creature.facing_y
                    if utils.is_in_world(tx, ty) and constants.WORLD[ty][tx] == "B":
                        self.output = (
                            constants.LONG_PROBE_DISTANCE - d + 1
                        ) / constants.LONG_PROBE_DISTANCE
                        break
                self.output = 0
            