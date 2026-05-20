def list_workflows(repo_url):
    print(f"Listing workflows for {repo_url}...")

def run_workflow(repo_url, workflow_name, dry_run=False):
    print(f"Running workflow {workflow_name} for {repo_url} (dry_run={dry_run})...")

def manage_workflows(repo_url, action='list'):
    print(f"Managing workflows for {repo_url}...")
