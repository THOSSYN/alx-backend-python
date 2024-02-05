#!/usr/bin/env python3
"""Test a dummy client"""

import requests
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from parameterized import parameterized_class
from utils import *
from client import *
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """A class that test a client"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, orgs_name, mocked_get_json):
        """A test case for the client 'GithubOrgClient.org'"""
        expected_url = f"https://api.github.com/orgs/{orgs_name}"
        mocked_get_json.return_value = {"some_data": "mocked up data"}
        
        git_org = GithubOrgClient(orgs_name)
        result = git_org.org

        mocked_get_json.assert_called_once_with(expected_url)
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

    def test_public_repos_url(self):
        """Test public repos url"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as Mocked_Org:
            Mocked_Org.return_value = {"repos_url": "https://api.github.com/orgs/example/repos"}
            git_org = GithubOrgClient('example')

            result = git_org._public_repos_url

            self.assertEqual(result, "https://api.github.com/orgs/example/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repo_url:
            get_json_result = [ 
                    {'name': 'truth'},
                    {'name': 'ruby-openid-apps-discovery'},
                    {'name': 'autoparse'}
            ]   
            mock_get_json.return_value = get_json_result
            expected_repos = [ 
                    'truth',
                    'ruby-openid-apps-discovery',
                    'autoparse']
            expected_url = "https://api.github.com/orgs/google/repos"
            mock_public_repo_url.return_value = expected_url

            git_org = GithubOrgClient('google')
            result = git_org.public_repos()

            mock_public_repo_url.assert_called_once_with()
            mock_get_json.assert_called_once_with(expected_url)
            self.assertEqual(result, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])  
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        git_org = GithubOrgClient('google')
        result = git_org.has_license(repo, license_key)
        print(result)

        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [
        (
            org_payload,
            repos_payload,
            expected_repos,
            apache2_repos
        ) for org_payload, repos_payload, expected_repos,
        apache2_repos in TEST_PAYLOAD
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing case"""
    @classmethod
    def setUpClass(cls):
        """A set up for testing"""
        cls.mock_requests_patcher = patch('requests.get')
        cls.mock_requests = cls.mock_requests_patcher.start()
        cls.mock_requests.json.side_effect = cls.repos_payload

    @classmethod
    def tearDownClass(cls):
        """A clen-up method for after-test"""
        cls.mock_requests_patcher.stop()

    def test_public_repos(self):
        """A test for public repos"""
        # self.mock_requests.json.side_effect = self.expected_repos
        # print(self.expected_repos)

        git_org = GithubOrgClient('google')
        result = git_org.public_repos()

        self.assertIsInstance(result, list)
        # self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests for public_repos with license"""
        pass


if __name__ == '__main__':
    unittest.main()
