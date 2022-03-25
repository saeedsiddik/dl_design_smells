from _ast import Call


class Conv2DCall:
    def __init__(self, ast_node: Call):
        self.ast_node = ast_node
        self.line_no = ast_node.lineno
        self.first_argument_value = ast_node.args[0].value

    def __str__(self):
        return f"Conv2D({self.first_argument_value}, ...) at line {self.line_no}"

    def __repr__(self):
        return self.__str__()
