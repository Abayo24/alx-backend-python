#!/usr/bin/env python3
"""TestGithubOrgClient class to test GithubOrgClient methods"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


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

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the
        correct URL based on the org payload"""

        # Use patch to mock the 'org' property
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            # Return a known payload for the org
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            # Initialize the client
            client = GithubOrgClient("google")

            # Access _public_repos_url
            result = client._public_repos_url

            # Assert that the result matches the expected URL
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")

        # Ensure the org property was called exactly once
        mock_org.assert_called_once()
