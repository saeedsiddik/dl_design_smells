import ast
from ast import NodeVisitor, literal_eval

class FindBatchNormDropoutCall(NodeVisitor):
    def __init__(self, *args):
        if len(args) < 1:
            raise ValueError("No target function (need at least one)")
        self.result = {arg: []for arg in args}

    def visit_Call(self, node):
        if hasattr(node.func, "id") and (node.func.id in self.result):
            self.result[node.func.id].append([node.lineno])
        # visit the children
        self.generic_visit(node)