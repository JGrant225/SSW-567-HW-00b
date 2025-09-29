import unittest
import requests
import json
from RepoReader import get_repo_info

class TestRepoReader(unittest.TestCase):

    def test_output_valid_user(self):
        import io
        import sys

        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        owner = "octocat"
        expected_output = (
            "Repo: boysenberry-repo-1 Number of commits: 4\n"
            "Repo: git-consortium Number of commits: 6\n"
            "Repo: hello-worId Number of commits: 1\n"
            "Repo: Hello-World Number of commits: 3\n"
            "Repo: linguist Number of commits: 30\n"
            "Repo: octocat.github.io Number of commits: 4\n"
            "Repo: Spoon-Knife Number of commits: 3\n"
            "Repo: test-repo1 Number of commits: 1\n"
        )

        get_repo_info(owner)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_output_invalid_user(self):
        import io
        import sys

        expected_output = "Failed to retrieve repos\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        owner = "thisuserdoesnotexist1234567890"

        get_repo_info(owner)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_commits_count(self):
        owner = "octocat"
        repo_name = "Hello-World"
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        commits = commits_response.json()

        self.assertEqual(commits_response.status_code, 200)
        self.assertEqual(len(commits), 3)

    

if __name__ == '__main__':
    unittest.main()
