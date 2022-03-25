from ast import NodeVisitor, literal_eval

from conv2D_call import Conv2DCall


class FindConv2DCall(NodeVisitor):
    results = []

    def visit_Call(self, node):
        if hasattr(node.func, "id") and (node.func.id == "Conv2D"):
            self.results.append(Conv2DCall(node))
            # self.result[node.func.id].append([node.lineno, node.args[0].value])
        # visit the children
        self.generic_visit(node)

    def find(self, node):
        self.visit(node)
        return self.results

