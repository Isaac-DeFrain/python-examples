import sys
import json
import asyncio
import pathlib
import python_graphql_client as pgc

# important paths
PARENT = pathlib.Path(__file__).parent
GITHUB_AUTH_TOK = PARENT / ".github_auth_tok"
QUERY_PATH = PARENT / ".graphql_query"
GITHUB_GRAPHQL = "https://api.github.com/graphql"

if __name__ == "__main__":

    if not GITHUB_AUTH_TOK.exists():
        print("GitHub auth token file does not exist..")
        print(f"Please add a GitHub auth token file {GITHUB_AUTH_TOK.name}")
        print("Exiting...")
        sys.exit(1)

    if not QUERY_PATH.exists():
        print("Query file does not exist..")
        print(f"Please add a query file {QUERY_PATH.name}")
        print("Exiting...")
        sys.exit(1)

    # github auth token and query files exist
    with GITHUB_AUTH_TOK.open("r") as t:
        auth_token = t.read()
        t.close()

    with QUERY_PATH.open("r") as q:
        query = q.read().strip()
        q.close()

    headers = {
        "Accept": "application/json",
        "Authorization": f"bearer {auth_token}"
    }
    client = pgc.GraphqlClient(endpoint=GITHUB_GRAPHQL, headers=headers)

    # print query
    print("~~~~~~~~~~~~~")
    print("~~~ Query ~~~")
    print("~~~~~~~~~~~~~")
    print(query)

    # print result
    print("~~~~~~~~~~~~~~")
    print("~~~ Result ~~~")
    print("~~~~~~~~~~~~~~")
    res = asyncio.run(client.execute_async(query))
    sorted_auth_error_keys = ['documentation_url', 'message']

    if not res.keys():
        print("Something went wrong!")
        print(f"res = {res}")
        sys.exit(1)

    if list(sorted(res.keys())) == sorted_auth_error_keys:
        # authentication error
        url = sorted_auth_error_keys[0]
        msg = sorted_auth_error_keys[1]
        print(res[msg])
        print(f"See {res[url]} for more information")
        sys.exit(1)

    else:
        print(json.dumps(res, indent=4))
        sys.exit(0)
