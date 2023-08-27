```python
import argparse
from github_oauth import github_oauth
from github_search_query import github_search_query

def main():
    parser = argparse.ArgumentParser(description='Search GitHub for code snippets.')
    parser.add_argument('--token', type=str, help='Your GitHub token.')
    parser.add_argument('--query', type=str, help='Your search query.')
    parser.add_argument('--language', type=str, help='The programming language of the code snippets.')
    parser.add_argument('--sort', type=str, help='The sort order of the search results.')

    args = parser.parse_args()

    token = args.token
    query_params = {
        'q': args.query,
        'language': args.language,
        'sort': args.sort
    }

    if github_oauth(token):
        search_results = github_search_query(token, query_params)
        print(search_results)
    else:
        print("Authentication failed. Please check your GitHub token.")

if __name__ == "__main__":
    main()
```