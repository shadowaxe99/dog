```python
import hashlib

def deduplicate_code(snippets):
    unique_snippets = {}
    for snippet in snippets:
        hash_object = hashlib.sha256(snippet.encode())
        hash_code = hash_object.hexdigest()
        if hash_code not in unique_snippets:
            unique_snippets[hash_code] = snippet
    return list(unique_snippets.values())
```