import subprocess
import tempfile
import os
import re


def validate_test_file(test_code: str) -> str:

    lines = test_code.splitlines()

    # Find individual test function blocks
    tests = []
    current_test = []

    for line in lines:

        if line.startswith("def test_"):

            if current_test:
                tests.append(current_test)

            current_test = [line]

        elif current_test:
            current_test.append(line)

    if current_test:
        tests.append(current_test)

    # Header + source code
    header = []
    for line in lines:
        if line.startswith("def test_"):
            break
        header.append(line)

    valid_tests = []

    for test in tests:

        test_block = "\n".join(header + test)

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as f:

            f.write(test_block)
            path = f.name

        try:

            result = subprocess.run(
                ["python", "-m", "pytest", path, "-q", "-p", "no:cacheprovider"],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                valid_tests.append(test)

        except subprocess.TimeoutExpired:
            pass

        finally:
            try:
                os.remove(path)
            except OSError:
                pass

    # Rebuild final file
    final_lines = header

    for test in valid_tests:
        final_lines.extend(test)
        final_lines.append("")

    return "\n".join(final_lines)