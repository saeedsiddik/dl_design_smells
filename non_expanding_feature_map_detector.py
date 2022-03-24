import ast
from pprint import pprint

from find_call import FindCall

if __name__ == '__main__':
    method_name = "Conv2D"
    #file = open('data/smell_sample/non_expanding_feature_maps/nefm_1.py', 'r')
    # file = open('data/non_smell_sample/1.py', 'r')
    file = open('data/smell_sample/non_expanding_feature_maps/googlenet.py', 'r')
    ast = ast.parse(file.read())

    fc = FindCall(method_name)
    fc.visit(ast)

    pprint(fc.result)

    for index in range(len(fc.result[method_name])-1):
        if fc.result[method_name][index][1] > fc.result[method_name][index+1][1]:
            print(f"Non-expanding feature map found at line {fc.result[method_name][index+1][0]}!")
