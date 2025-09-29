import requests
import json

def get_repo_info(owner):
    repo_url = f"https://api.github.com/users/{owner}/repos"
    repo_response = requests.get(repo_url)

    if repo_response.status_code == 200:
        repos = repo_response.json()
        for repo in repos:
            name = repo['name']
            commits_url = f"https://api.github.com/repos/{owner}/{name}/commits"
            commits_response = requests.get(commits_url)

            if commits_response.status_code == 200:
                num_commits = len(commits_response.json())
                print(f"Repo: {name} Number of commits: {num_commits}")
            else:
                print(f"Failed to retrieve commits for repo: {name}")
    else:
        print(f"Failed to retrieve repos")
    return
    


if __name__ == "__main__":
    get_repo_info("octocat")