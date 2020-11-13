import requests


class GitRepos:

    def repos_with_stars(self, value, language):
        params = {"q": f"stars:>{value} language:{language}"}
        print(params)
        response = requests.get("https://api.github.com/search/repositories", params=params)
        items = response.json()["items"]
        # print("response code from git", response.status_code)
        # print("response from git", response.json()["items"])

        print ('\n'.join([ f"{item['name']} has {item['stargazers_count']} starts" for item in items]))

    

if __name__ == "__main__":
    repo = GitRepos()
    repo.repos_with_stars(150000, "javascript")
