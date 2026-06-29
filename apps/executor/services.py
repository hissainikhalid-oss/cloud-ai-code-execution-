import subprocess
import tempfile
import os
import time


def execute_python(code: str, user_input: str = "") -> dict:
    """
    Execute Python code safely and return output.
    """

    with tempfile.NamedTemporaryFile(
        suffix=".py",
        delete=False,
        mode="w",
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(code)
        temp_filename = temp_file.name

    start_time = time.time()

    try:
        result = subprocess.run(
            ["python", temp_filename],
            input=user_input,
            text=True,
            capture_output=True,
            timeout=10
        )

        execution_time = round(time.time() - start_time, 3)

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "execution_time": execution_time,
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "output": "",
            "error": "Execution timed out.",
            "execution_time": 10,
        }

    finally:

        if os.path.exists(temp_filename):
            os.remove(temp_filename)