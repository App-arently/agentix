# orchestrator.py

from specialized_agents import (
    FrontendAgent,
    BackendAgent,
    DatabaseAgent,
    TaskDecomposer,
    CodeReviewer,
    CodeEvaluator,
    TestGenerator,
    GameDevelopmentAgent,

    
)
from git import Repo, GitCommandError
import os
import json
import logging
from dashboard.dashboard_app import send_update, start_dashboard
from celery import Celery
from config import Config
import ssl
from utils import validate_code_syntax, integrate_code

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Celery
celery_app = Celery('orchestrator', broker='redis://localhost:6379/0')
celery_app.conf.update(
    result_backend='redis://localhost:6379/0',
    #result_backend=Config.CELERY_RESULT_BACKEND,
)
celery_app.conf.broker_connection_retry_on_startup = True

class Orchestrator:
    def __init__(self):
        self.agents = {
            'frontend': FrontendAgent(),
            'backend': BackendAgent(),
            'database': DatabaseAgent(),
            'game_development': GameDevelopmentAgent(),
        }
        self.task_decomposer = TaskDecomposer()
        self.code_reviewer = CodeReviewer()
        self.code_evaluator = CodeEvaluator()
        self.test_generator = TestGenerator()
        self.repo = Repo('.')
        self.current_branch = self.repo.active_branch.name
        self.project_tasks = []
        start_dashboard()

    def decompose_project(self, description):
        tasks = self.task_decomposer.decompose_project(description)
        self.project_tasks = tasks
        return tasks

    def run(self, project_description):
        send_update(f"Starting new project: {project_description}")
        tasks = self.decompose_project(project_description)
        for task in tasks:
            send_update(f"Queueing task: {task['task']}")
            execute_task.delay(task, self.repo.git_dir)
        send_update("All tasks have been queued.")

    def save_project_state(self, filename='project_state.json'):
        state = {
            'tasks': self.project_tasks,
            'files': [item.a_path for item in self.repo.index.diff(None)],
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)

    def load_project_state(self, filename='project_state.json'):
        with open(filename, 'r') as f:
            state = json.load(f)
            self.project_tasks = state.get('tasks', [])
            return state

@celery_app.task
def execute_task(task, repo_path):
    logging.info(f"Executing task: {task['task']}")
    orchestrator = Orchestrator()
    orchestrator.repo = Repo(repo_path)
    orchestrator.current_branch = orchestrator.repo.active_branch.name
    send_update(f"Working on task: {task['task']}")
    try:
        create_branch(orchestrator.repo, task)
        agent = orchestrator.agents.get(task['type'])
        if not agent:
            send_update(f"No agent found for task type: {task['type']}")
            return
        code = agent.generate_code(task['task'])
        if code:
            is_valid = validate_code_syntax(code, task['type'])
            if is_valid:
                integrate_code(code, task)
                commit_changes(orchestrator.repo, task)
                create_pull_request(orchestrator.repo.active_branch.name)
            else:
                send_update(f"Code validation failed for task: {task['task']}")
        else:
            send_update(f"No code generated for task: {task['task']}")
    except Exception as e:
        logging.error(f"Error executing task {task['task']}: {e}")
    finally:
        checkout_main_branch(orchestrator.repo, orchestrator.current_branch)

def create_branch(repo, task):
    branch_name = f"{task['type']}/{task['task'].replace(' ', '_').lower()}"
    try:
        repo.git.checkout('HEAD', b=branch_name)
    except GitCommandError:
        repo.git.checkout(branch_name)
    send_update(f"Checked out to branch: {branch_name}")

def commit_changes(repo, task):
    try:
        repo.git.add(A=True)
        repo.index.commit(f"AI generated code for {task['type']} task: {task['task']}")
        send_update(f"Committed changes for task: {task['task']}")
    except Exception as e:
        logging.error(f"Error committing changes: {e}")

def create_pull_request(branch_name):
    # Placeholder for actual pull request creation
    send_update(f"Creating pull request for branch: {branch_name}")

def checkout_main_branch(repo, main_branch_name):
    repo.git.checkout(main_branch_name)
