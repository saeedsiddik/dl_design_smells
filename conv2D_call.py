from _ast import Call

from find_argument import FindArgument


class Conv2DCall:
    def __init__(self, ast_node: Call):
        self.ast_node = ast_node
        self.line_no = ast_node.lineno
        if len(ast_node.args) > 0:
            self.filters_value = ast_node.args[0].value
        else:
            self.filters_value = FindArgument().find(ast_node)

    def __str__(self):
        return f"Conv2D({self.filters_value}, ...) at line {self.line_no}"

    def __repr__(self):
        return self.__str__()
