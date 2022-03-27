from ast import NodeVisitor

from conv2D_call import Conv2DCall


class FindConv2DCall(NodeVisitor):
    def __init__(self):
        self.results = []

    def visit_Call(self, node):
        func = node.func
        if (hasattr(func, "id") and (func.id == "Conv2D")) or \
                (hasattr(func, "attr") and func.attr == "Conv2D"):
            self.results.append(Conv2DCall(node))
        self.generic_visit(node)

    def find(self, node):
        self.visit(node)
        return self.results

