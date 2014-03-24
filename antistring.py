# see http://blog.sigfpe.com/2012/03/overloading-python-list-comprehension.html

from ast import *
import sys

class RewriteComp(NodeTransformer):
    def visit_func(self, node):
        print dump(node)
        return node

    def visit_Str(self, node):
        print dump(node)
        namenode = Name(id="FreeString", lineno=node.lineno, col_offset=node.col_offset, ctx=Load())

        newnode = Call(func=namenode, keywords=[], args=[node],
                       lineno=node.lineno, col_offset=node.col_offset)
        return newnode

source = open(sys.argv[1]).read()
e = compile(source, "<string>", "exec", PyCF_ONLY_AST)
print dump(e)
#print e
e = RewriteComp().visit(e)
f = compile(e, sys.argv[1], "exec")
#print f
exec f
print "Done"
