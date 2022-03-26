from _ast import FunctionDef, If, Compare, Eq, Name, Constant
from ast import NodeVisitor

from find_call import FindConv2DCall


class FindDefinition(NodeVisitor):
    results = []

    def visit_FunctionDef(self, node: FunctionDef):
        conv2ds = FindConv2DCall().find(node)
        self.results.append(conv2ds)
        self.generic_visit(node)

    def visit_If(self, node: If):
        if type(node.test) is Compare:
            test: Compare = node.test
            if type(test.ops[0]) is Eq and type(test.left) is Name and type(test.comparators[0]) is Constant:
                if test.left.id == "__name__" and test.comparators[0].value == "__main__":
                    conv2ds = FindConv2DCall().find(node)
                    self.results.append(conv2ds)
        self.generic_visit(node)
