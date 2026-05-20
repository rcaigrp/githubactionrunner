import requests

def list_workflows(owner, repo, token=None):
    """List workflows for a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [wf['name'] for wf in response.json().get('workflows', [])]

def run_workflow(owner, repo, workflow_name, ref, token=None):
    """Run a workflow."""
    # Find workflow ID
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    workflow_id = None
    for wf in data.get('workflows', []):
        if wf['name'] == workflow_name:
            workflow_id = wf['id']
            break
    if not workflow_id:
        raise ValueError(f"Workflow {workflow_name} not found")
    
    # Run workflow
    run_url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatch"
    payload = {"ref": ref}
    resp = requests.post(run_url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json().get('id')

def manage_workflows(owner, repo, action):
    """Manage workflows."""
    return "ok"
