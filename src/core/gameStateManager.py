from src.core.stateMachine import StateMachine

class GameStateManager:
    def __init__(self, jsonStateMachines, control):
        self.machines = {}
        self.control = control
        self._init_states(jsonStateMachines)


    def _init_states(self, jsonStateMachines):
        for itterStateMachine in jsonStateMachines:
            # Create StateMachine:
            self.machines[itterStateMachine] = StateMachine()

            # ADD NODES:
            for itterNodes in jsonStateMachines[itterStateMachine]["states"]:
                self.machines[itterStateMachine].addNode(itterNodes)

            # ADD Edges
            for itterEdges in jsonStateMachines[itterStateMachine]["conections"]:
                try:
                    a,b,condition,key = str(itterEdges).split(":")

                    if condition == "symbol":
                        self.machines[itterStateMachine].addConection(a,b,key)
                        continue

                    if condition == "controls":
                        if key == "direction_buttons":
                            for key_code in self.control.direction_buttons:
                                self.machines[itterStateMachine].addConection(a, b, key_code)
                                continue

                        if key == "action_buttons":
                            for key_code in self.control.action_buttons:
                                self.machines[itterStateMachine].addConection(a, b, key_code)
                                continue

                        key_code = getattr(self.control, key)
                        self.machines[itterStateMachine].addConection(a, b, key_code)
                except:
                    pass

            self.machines[itterStateMachine].setInitialPointer(jsonStateMachines[itterStateMachine]["initial"])


    def getStateMachine(self, key):
        stateMachine = None

        try:
            return self.machines[key]
        except:
            pass

        return stateMachine


    def update_state(self):
        pass


    def verifyStateMachines(self):
        print(f"Total Machines: {len(self.machines)}")
        for i in self.machines:
            print(f"Machine: {i}\nPointer: {self.machines[i].pointer}\nNodes: {self.machines[i].node}\nEdges: {self.machines[i].edges}\n\n")
