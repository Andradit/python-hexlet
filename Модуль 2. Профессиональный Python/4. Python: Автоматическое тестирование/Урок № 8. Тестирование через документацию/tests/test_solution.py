import subprocess


def test_reverse():
    assert subprocess.run(["python", "src/solution.py", "-v"]).returncode == 0