import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('owner')
@click.argument('repo')
@click.argument('token')
def list_workflows(owner, repo, token):
    """List workflows for a repository."""
    from GitHubActionRunner import list_workflows as _list
    workflows = _list(owner, repo, token)
    for w in workflows:
        click.echo(w)

@cli.command()
@click.argument('owner')
@click.argument('repo')
@click.argument('workflow_name')
@click.argument('ref')
@click.argument('token')
def run_workflow(owner, repo, workflow_name, ref, token):
    """Run a workflow."""
    from GitHubActionRunner import run_workflow as _run
    job_id = _run(owner, repo, workflow_name, ref, token)
    click.echo(f"Started workflow: {job_id}")
