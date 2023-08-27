```python
import requests

def github_search_query(token, query_params):
    headers = {'Authorization': f'token {token}'}
    url = "https://api.github.com/search/code"
    response = requests.get(url, headers=headers, params=query_params)
    return response.json()
```