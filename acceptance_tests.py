import responses
import pytest
from github_action_runner.github_client import GitHubClient

MOCK_WORKFLOWS = {
    "workflows": [
        {"name": "test_workflow", "id": 1},
        {"name": "build_workflow", "id": 2}
    ]
}

class TestGitHubClient:
    @responses.activate
    def test_list_workflows(self):
        url = "https://api.github.com/repos/owner/repo/actions/workflows"
        responses.add(
            responses.GET, 
            url, 
            json=MOCK_WORKFLOWS, 
            status=200
        )
        client = GitHubClient(token="fake_token")
        workflows = client.list_workflows("owner/repo")
        assert len(workflows) == 2
        assert workflows[0]['name'] == "test_workflow"

    @responses.activate
    def test_trigger_workflow(self):
        url = "https://api.github.com/repos/owner/repo/actions/workflows/build_workflow/dispatch"
        responses.add(
            responses.POST, 
            url, 
            json={"id": 123}, 
            status=204
        )
        client = GitHubClient(token="fake_token")
        result = client.trigger_workflow("owner/repo", "build_workflow")
        assert result == {"id": 123}
