import requests

class GitHubClient:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com/repos/"
        self.token = token
        
    def _get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    def list_workflows(self, repo):
        url = f"{self.base_url}{repo}/actions/workflows"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get("workflows", [])

    def trigger_workflow(self, repo, workflow_name):
        url = f"{self.base_url}{repo}/actions/workflows/{workflow_name}/dispatch"
        payload = {"ref": "main"}
        response = requests.post(url, headers=self._get_headers(), json=payload)
        response.raise_for_status()
        return response.json()
