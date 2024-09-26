# utils.py

import subprocess
import os
import logging
from dashboard.dashboard_app import send_update

def validate_code_syntax(code, task_type):
    if task_type == 'frontend':
        # Use ESLint for JavaScript/React code
        with open('temp_code.js', 'w') as f:
            f.write(code)
        result = subprocess.run(['eslint', 'temp_code.js'], capture_output=True, text=True)
        os.remove('temp_code.js')
        if result.returncode != 0:
            logging.error(f"ESLint errors:\n{result.stderr}")
            return False
        return True
    elif task_type == 'backend':
        # Use flake8 for Python code
        with open('temp_code.py', 'w') as f:
            f.write(code)
        result = subprocess.run(['flake8', 'temp_code.py'], capture_output=True, text=True)
        os.remove('temp_code.py')
        if result.returncode != 0:
            logging.error(f"Flake8 errors:\n{result.stderr}")
            return False
        return True
    elif task_type == 'database':
        # For SQL, basic syntax check can be implemented if necessary
        return True  # Simplification
    else:
        return False

def integrate_code(code, task):
    filename = f"{task['type']}_{task['task'].replace(' ', '_').lower()}"
    if task['type'] == 'frontend':
        filename += '.jsx'
    elif task['type'] == 'backend':
        filename += '.py'
    elif task['type'] == 'database':
        filename += '.sql'
    else:
        filename += '.txt'
    with open(filename, 'w') as f:
        f.write(code)
    send_update(f"Generated code for {task['type']} task: {task['task']}")
    send_update(f"Generated code:\n{code}")
