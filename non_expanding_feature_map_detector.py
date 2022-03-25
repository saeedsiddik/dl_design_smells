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
    calls = get_conv2d_calls_in_groups()

    print(calls)
    # for dec in declarations:
    #     fc = FindCall(method_name)
    #     fc.visit(dec)
    #
    # pprint(fc.result)
    #
    # for index in range(len(fc.result[method_name])-1):
    #     if fc.result[method_name][index][1] > fc.result[method_name][index+1][1]:
    #         print(f"Non-expanding feature map found at line {fc.result[method_name][index+1][0]}!")
