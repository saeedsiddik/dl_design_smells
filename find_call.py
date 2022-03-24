from ast import NodeVisitor, literal_eval


class FindCall(NodeVisitor):
    def __init__(self, *args):
        if len(args) < 1:
            raise ValueError("Must supply at least ine target function")
        self.result = {arg: []for arg in args}

    def visit_Call(self, node):
        if hasattr(node.func, "id") and (node.func.id in self.result):
            self.result[node.func.id].append([node.lineno, node.args[0].value])
        # visit the children
        self.generic_visit(node)