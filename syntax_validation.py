```python
import subprocess
import os

def validate_syntax(file_path):
    result = subprocess.run(['flake8', file_path], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# Example usage
# errors = validate_syntax('your_python_file.py')
# if errors:
#     print(errors)
# else:
#     print("No syntax errors found.")
```