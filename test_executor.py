from apps.executor.services import execute_python

code = """
print(x)
"""

result = execute_python(code)

print(result)