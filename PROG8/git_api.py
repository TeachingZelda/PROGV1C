import requests

uri = "https://api.github.com/users/zedlord/repos"

response = requests.get(uri)

repositories = response.json()
print(repositories)

for repo in repositories:
    print("Naam:", repo["name"])
    print("Beschrijving:", repo["description"])
    print("Programmeertaal:", repo["language"])
    print("Sterren:", repo["stargazers_count"])
    print("URL:", repo["html_url"])
    print("-" * 40)
