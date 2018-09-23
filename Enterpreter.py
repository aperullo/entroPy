#This class will be the interpreter that transforms normal python programs into programs using the entroPy classes.

#http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html

import ast
import os
from Float import Float
from Integer import Integer
from String import String
import astor

#replaces all primitive types with calls to the entropy classes
#TODO: one test to verify its working, value shouldnt change if its only read once
class entTransformer(ast.NodeTransformer):

    _entropy_types = ["Boolean", "Float", "Char", "String", "Integer"]

    #all nodes of type Num are automatically converted into float or int type
    def visit_Num(self, node):
        self.generic_visit(node)
        # print(node)
        # print(node.n)
        # print(type(node.n))

        #TODO: can probably shorten this down to just a line with a ternary in the ID
        if isinstance(node.n, float):  # if node value is a float, call the Float constructor over it.
            return ast.Call(func=ast.Name(id='Float', ctx=ast.Load()), args=[ast.Num(n=node.n)], keywords=[])
        elif isinstance(node.n, int):  # if node value is a int, call the Integer constructor over it.
            return ast.Call(func=ast.Name(id='Integer', ctx=ast.Load()), args=[ast.Num(n=node.n)], keywords=[])
        else:  # if node value was somehow neither, don't touch it
            return node


    def visit_Str(self, node):
        self.generic_visit(node)
        # print(node)
        # print(node.s)
        # print(type(node.s))

        if isinstance(node.s, str): # if node value is a str, call the String constructor over it.
            return ast.Call(func=ast.Name(id='String', ctx=ast.Load()), args=[ast.Str(s=node.s)], keywords=[])
        else:  # if node value was somehow not a str, don't touch it
            return node

    #all nodes of type NameConstant are checked for being booleans and converted. If not they are left alone.
    def visit_NameConstant(self, node):
        self.generic_visit(node)
        # print(node)
        # print(node.value)
        # print(type(node.value))

        if isinstance(node.value, bool): # if node value is a bool, call the Boolean constructor over it.
            return ast.Call(func=ast.Name(id='Boolean', ctx=ast.Load()), args=[ast.NameConstant(value=node.value)], keywords=[])
        else:  # if node value was not a bool (IE was NoneType), don't touch it.
            return node

    def visit_Call(self, node):
        self.generic_visit(node)
        # print(node)
        # print(node.func)
        # print(type(node.func))

        # some builtins enforce and coerce. For example, len("hi") coerces the result to an int, so wrap the result in an entropy Integer
        # I may have to extend this as I find more builtins with sanity checks that force types. Or until I find a better solution.
        if (isinstance(node.func, ast.Name) and     # if the nodes function is an ast.name
            isinstance(node.func.id, str) and       # and if the id of that name is a str (sanity check)
            node.func.id == "len"):                 # and if the id of that name is len (builtin len())

            return ast.Call(func=ast.Name(id='Integer', ctx=ast.Load()), args=[node], keywords=[])  #Wrap the node itself in an Integer call
        else:
            return node
        

    # Unused: was going to changes usage of variable x to x.val since entropy types are wrappers. Causes issues and seems to be unnecessary.
    # def visit_Name(self, node):
    #     self.generic_visit(node)
    #     #print(node, node.id, node.ctx)
    #
    #     if node.id in self._entropy_types and isinstance(node.ctx, ast.Load):
    #
    #         return ast.Call(func=ast.Attribute(value=ast.Name(id='a', ctx=ast.Load()), attr='getval', ctx=ast.Load()), args=[], keywords=[])
    #
    #         #return ast.Attribute(value=ast.Name(id=node.id, ctx=ast.Load()), attr='val', ctx=ast.Load())
    #         # return ast.Call(func=ast.Name(id='Boolean', ctx=ast.Load()), args=[ast.NameConstant(value=node.value)],
    #         #                 keywords=[])
    #     return node

    # Unused: was going to look at all nodes and type check them. visit_CLASS is more elegant
    # def visit(self, node):
    #     self.generic_visit(node)
    #     #Since we are modifying types, we only care about where variables are assigned and used.
    #     #Ctx only exists where a variable does, and we only care if it is one of (Store, Load).
    #
    #     for child in ast.iter_child_nodes(node):
    #         if hasattr(child, "ctx") and isinstance(child.ctx, ast.Load):
    #             print(node, child, child.ctx)
    #
    #     # """Visit a node."""
    #     # method = 'visit_' + node.__class__.__name__
    #     # visitor = getattr(self, method, self.generic_visit)
    #     # return visitor(node)
    #
    #     ast.Load
    #     # print(node.n)
    #     # print(type(node.n))
    #     return node


def main():
    path = "F:\\dev\\git\\entroPy\\test.py"
    source_code = open(path).read()
    #print(source_code)

    a = ast.parse(source_code)
    entTransformer().visit(a)
    ast.fix_missing_locations(a)
    co = compile(a, '<ast>', 'exec')
    #print(astor.dump_tree(a))
    print(astor.to_source(a))
    exec(co)

main()