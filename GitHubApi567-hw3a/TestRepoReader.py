import unittest
import requests
from unittest.mock import patch, Mock
import json
from RepoReader import get_repo_info
import io
import sys

class TestRepoReader(unittest.TestCase):

    def _mock_response(self, status_code, json_data):
        mock_resp = Mock()
        mock_resp.status_code = status_code
        mock_resp.json = Mock(return_value=json_data)
        return mock_resp

    @patch('RepoReader.requests.get')
    def test_output_valid_user(self, mock_get):
        mock_get.side_effect = [
            self._mock_response(200, [{"name": "Repo1"}, {"name": "Repo2"}]),
            self._mock_response(200, [{"commit": "data1"}, {"commit": "data2"}]),
            self._mock_response(200, [{"commit": "data1"}])
        ]

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_repo_info("fakeuser")

        sys.stdout = sys.__stdout__

        expected_output = (
            "Repo: Repo1 Number of commits: 2\n"
            "Repo: Repo2 Number of commits: 1\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch('RepoReader.requests.get')
    def test_output_invalid_user(self, mock_get):

        mock_get.return_value = self._mock_response(404, {})

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_repo_info("doesnotexist")

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Failed to retrieve repos\n")

    @patch('RepoReader.requests.get')
    def test_commits_invalid(self, mock_get):
        mock_get.side_effect = [
            self._mock_response(200, [{"name": "Repo1"}]),
            self._mock_response(500, {})
        ]

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_repo_info("fakeuser")

        sys.stdout = sys.__stdout__
        self.assertEqual(
            captured_output.getvalue(),
            "Failed to retrieve commits for repo: Repo1\n"
        )

    

if __name__ == '__main__':
    unittest.main()
