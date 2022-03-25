import ast
from pprint import pprint

from find_definition import FindDefinition
from find_call import FindConv2DCall


def get_ast():
    # file = open('data/smell_sample/non_expanding_feature_maps/nefm_1.py', 'r')
    # file = open('data/non_smell_sample/1.py', 'r')
    file = open('data/smell_sample/non_expanding_feature_maps/googlenet.py', 'r')
    return ast.parse(file.read())


def get_conv2d_calls_in_groups():
    fd = FindDefinition()
    fd.visit(ast)
    return fd.results


if __name__ == '__main__':
    method_name = "Conv2D"

    ast = get_ast()
    call_groups = get_conv2d_calls_in_groups()

    print(call_groups)
    for calls in call_groups:
        for i in range(len(calls)-1):
            if calls[i].first_argument_value > calls[i+1].first_argument_value:
                print(f"Non-expanding feature map found at line {calls[i+1].line_no}!")