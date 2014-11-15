import ast

codigo = 'def suma(x, y):' + 'return x  + y'


module = ast.parse(codigo)
import ipdb; ipdb.set_trace()