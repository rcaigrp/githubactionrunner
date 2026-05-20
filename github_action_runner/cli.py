import click
from github_action_runner.github_client import GitHubClient

@click.group()
def cli():
    """GitHubActionRunner CLI entry point."""
    pass

@cli.command()
@click.option('--repo', required=True, help='Repository URL')
@click.option('--token', help='GitHub Token')
def list_workflows(repo, token):
    """List workflows for a repository."""
    client = GitHubClient(token)
    workflows = client.list_workflows(repo)
    for wf in workflows:
        click.echo(wf['name'])

@cli.command()
@click.option('--repo', required=True, help='Repository URL')
@click.option('--workflow', required=True, help='Workflow name')
@click.option('--token', help='GitHub Token')
def run_workflow(repo, workflow, token):
    """Run a workflow."""
    client = GitHubClient(token)
    client.trigger_workflow(repo, workflow)
    click.echo(f"Workflow {workflow} triggered for {repo}")

if __name__ == "__main__":
    cli()
