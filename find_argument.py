from _ast import keyword
from ast import NodeVisitor


class FindArgument(NodeVisitor):
    result = int

    def visit_keyword(self, node: keyword):
        if node.arg == 'filters':
            self.result = node.value.value

    def find(self, node):
        self.visit(node)
        return self.result
