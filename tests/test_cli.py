import subprocess

def run_cli(*args):
    """
    Helper function to run the CLI application and capture the output.
    """
    process = subprocess.run(
        ['pass'] + list(args),
        capture_output=True,
        text=True
    )
    process.communicate("")
    return result

def test_greet():
    result = run_cli('--greet', 'John')
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, John!"
    assert result.stderr == ""
