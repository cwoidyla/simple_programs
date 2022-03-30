from collections import OrderedDict
from itertools import starmap, product
from turtle import pos

class ParameterCombinator:
    def __init__(self):
        self.parameter_space = OrderedDict()
        self.param_vectors = []

    def add_parameter_space(self, name, possible_values):
        assert type(name) == str and type(possible_values) == list
        self.parameter_space[name] = possible_values

    def create_param_combos(self):
        test_space = list(tuple(i for i in self.parameter_space.values()))
        itertools_starmap_obj = starmap(product, [test_space])
        for obj in list(itertools_starmap_obj):
            self.param_vectors += list(obj)

if __name__ == '__main__':
    pc = ParameterCombinator()
    pc.add_parameter_space('letters', ['a','b','c','d'])
    pc.add_parameter_space('numbers', ['1','2','3','4'])
    pc.add_parameter_space('special_chars', ['!','@','#','$'])
    pc.create_param_combos()
    print(pc.param_vectors)
