import click

@click.command()
@click.argument('repo_url')
@click.argument('workflow_name')
@click.option('--dry-run', is_flag=True)
def main(repo_url, workflow_name, dry_run=False):
    pass

if __name__ == '__main__':
    main()
