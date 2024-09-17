#!/usr/bin/env python3
"""TestGithubOrgClient class to test GithubOrgClient methods"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict, List


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient methods"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self,
                 org_name: str,
                 expected_response: Dict[str, str],
                 mock_get_json: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)

        result: Dict[str, str] = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, expected_response)

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns the
        correct URL based on the org payload"""

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            client = GithubOrgClient("google")

            result: str = client._public_repos_url

            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")

        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.public_repos
        returns the expected repos
        """
        mock_get_json.return_value = [{"name": "repo1",
                                       "license": {"key": "mit"}
                                       },
                                      {"name": "repo2",
                                       "license": {"key": "apache"}
                                       },
                                      {"name": "repo3",
                                       "license": {"key": "mit"}
                                       },
                                      ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'https://api.github.com/orgs/google/repos'

            client = GithubOrgClient('google')

            result: List[str] = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/google/repos'
                )

    @parameterized.expand([
        ({'license': {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self,
                         repo: Dict,
                         license_key: str,
                         expected: bool) -> None:
        """
        Test that GithubOrgClient.has_license
        returns the correct value
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
