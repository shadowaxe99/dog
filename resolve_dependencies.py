```python
import subprocess

def resolve_dependencies(dependencies):
    for dep in dependencies:
        subprocess.run(["pip", "install", dep])
```