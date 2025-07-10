import subprocess
import tempfile
import json
import os
import shlex

def _run_plain(tmp_path: str):
    import sys
    return subprocess.run([
        sys.executable, tmp_path
    ], capture_output=True, text=True)


def execute_script(script: str):
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as tmp:
        tmp.write(script)
        tmp.flush()

        cmd = [
            'nsjail',
            '--quiet',
            '--disable_clone_newnet',
            '--time_limit', '5',
            '--rlimit_as', '512',
            '--disable_proc', 'false',   
            '--chroot', '/',
            '--log_fd', '2',
            '--exec_file', '/usr/bin/python3',
            '--',
            tmp.name,
        ]

        

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
        except Exception as jail_err:
            result = _run_plain(tmp.name)

        if result.returncode != 0:
            plain = _run_plain(tmp.name)
            if plain.returncode != 0:
                raise Exception(f"Script execution failed (nsjail and plain):\n{result.stderr}\n{plain.stderr}")
            result = plain

        try:
            output_lines = [l for l in result.stdout.strip().split('\n') if l]
            for line in reversed(output_lines):
                try:
                    result_json = json.loads(line)
                    return result_json, result.stdout
                except json.JSONDecodeError:
                    continue
            raise Exception("main() must return a valid JSON object")
        except Exception:
            raise Exception("main() must return a valid JSON object")
