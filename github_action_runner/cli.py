import click
from github_action_runner import core

@click.group()
def cli():
    """GitHubActionRunner CLI tool"""
    pass

@cli.command()
@click.argument('repo_url')
@click.argument('workflow_name')
@click.option('--dry-run', is_flag=True, default=False, help='Run in dry-run mode')
def run(repo_url, workflow_name, dry_run):
    """List, run, and manage workflows."""
    click.echo(f"Repository: {repo_url}")
    click.echo(f"Workflow: {workflow_name}")
    click.echo(f"Dry Run: {dry_run}")
    core.list_workflows(repo_url)
    core.run_workflow(repo_url, workflow_name, dry_run)

if __name__ == '__main__':
    cli()
