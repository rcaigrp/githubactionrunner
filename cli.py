import click

@click.group()
def main():
    """GitHubActionRunner CLI"""
    pass

@main.command()
@click.argument('repo_url')
@click.argument('workflow_name')
@click.option('--dry-run', is_flag=True, help='Run in dry-run mode')
def run(repo_url, workflow_name, dry_run):
    """Run a workflow"""
    click.echo(f"Running {workflow_name} on {repo_url} (dry-run={dry_run})")

@main.command()
@click.argument('repo_url')
def list(repo_url):
    """List workflows"""
    click.echo(f"Listing workflows for {repo_url}")

@main.command()
@click.argument('repo_url')
def manage(repo_url):
    """Manage workflows"""
    click.echo(f"Managing workflows for {repo_url}")

if __name__ == '__main__':
    main()
