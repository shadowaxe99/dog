```python
import requests

def github_oauth(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        return True
    return False
```