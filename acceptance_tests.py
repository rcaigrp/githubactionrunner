import subprocess
import os
import sys


def test_criterion_1_cli_entry_point():
    """Test CLI entry point runs successfully."""
    env = os.environ.copy()
    env['PYTHONPATH'] = '/workspace/projects'
    result = subprocess.run(['python', '-m', 'GitHubActionRunner', '--help'], capture_output=True, text=True, env=env)
    assert result.returncode == 0, f"CLI entry point failed: {result.stderr}"
    assert 'GitHubActionRunner' in result.stdout


def test_criterion_2_parse_repo_url():
    """Test parsing repository URL argument."""
    env = os.environ.copy()
    env['PYTHONPATH'] = '/workspace/projects'
    result = subprocess.run(['python', '-m', 'GitHubActionRunner', 'run', 'https://github.com/test/repo', 'workflow.yml'], capture_output=True, text=True, env=env)
    assert result.returncode == 0, f"CLI failed with repo URL: {result.stderr}"


def test_criterion_3_parse_workflow_name():
    """Test parsing workflow name argument."""
    env = os.environ.copy()
    env['PYTHONPATH'] = '/workspace/projects'
    result = subprocess.run(['python', '-m', 'GitHubActionRunner', 'run', 'https://github.com/test/repo', 'workflow.yml'], capture_output=True, text=True, env=env)
    assert result.returncode == 0, f"CLI failed with workflow name: {result.stderr}"


def test_criterion_4_parse_dry_run_flag():
    """Test parsing dry-run mode flag."""
    env = os.environ.copy()
    env['PYTHONPATH'] = '/workspace/projects'
    result = subprocess.run(['python', '-m', 'GitHubActionRunner', 'run', 'https://github.com/test/repo', 'workflow.yml', '--dry-run'], capture_output=True, text=True, env=env)
    assert result.returncode == 0, f"CLI failed with dry-run flag: {result.stderr}"


def test_criterion_5_placeholder_functions():
    """Test placeholder functions exist."""
    from GitHubActionRunner import list_workflows, run_workflow, manage_workflow
    assert callable(list_workflows)
    assert callable(run_workflow)
    assert callable(manage_workflow)
