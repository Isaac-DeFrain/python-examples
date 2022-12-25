import asyncio
from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint="https://api.github.com/graphql")
query = '''
    query {
        repository(owner:"octocat", name:"Hello-World") {
            issues(last:20, states:CLOSED) {
                edges {
                    node {
                        title
                        url
                        labels(first:5) {
                            edges {
                                node {
                                    name
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    '''.strip()
print("Query:")
print(query)
res = asyncio.run(client.execute_async(query))
print(res)
