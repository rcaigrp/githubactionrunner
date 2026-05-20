import unittest
import responses

import sys
sys.path.insert(0, '/workspace/projects')

from GitHubActionRunner import list_workflows, run_workflow

class TestGitHubActionRunner(unittest.TestCase):
    @responses.activate
    def test_list_workflows(self):
        responses.add(
            responses.GET,
            "https://api.github.com/repos/test/test/actions/workflows",
            json={"workflows": [{"name": "ci", "id": 1}, {"name": "deploy", "id": 2}]}
        )
        result = list_workflows("test", "test", "token")
        self.assertEqual(result, ["ci", "deploy"])

    @responses.activate
    def test_run_workflow(self):
        # Mock list workflows to find the ID
        responses.add(
            responses.GET,
            "https://api.github.com/repos/test/test/actions/workflows",
            json={"workflows": [{"name": "ci", "id": 1}]}
        )
        # Mock run workflow
        responses.add(
            responses.POST,
            "https://api.github.com/repos/test/test/actions/workflows/1/dispatch",
            json={"id": 12345}
        )
        job_id = run_workflow("test", "test", "ci", "main", "token")
        self.assertEqual(job_id, 12345)

if __name__ == '__main__':
    unittest.main()
