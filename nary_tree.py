class n_node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, val):
        self.children.append(n_node(val))

    def get_children(self):
        return self.children

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def __str__(self):
        return str(f'[{self.val} {", ".join([str(child) for child in self.children])}]')