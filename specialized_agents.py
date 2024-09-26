# specialized_agents.py

from base_agent import BaseAgent
import json
import logging

class FrontendAgent(BaseAgent):
    def create_prompt(self, task_description):
        task_description = self.sanitize_input(task_description)
        return f"""
You are an expert React.js developer.

Task:
{task_description}

Requirements:
- Use functional components with hooks.
- Ensure the code is complete and syntactically correct.
- Include necessary imports.
- Follow best practices and code style guidelines.

Provide the code only, without additional explanations.
"""

class BackendAgent(BaseAgent):
    def create_prompt(self, task_description):
        task_description = self.sanitize_input(task_description)
        return f"""
You are an expert Python backend developer using FastAPI.

Task:
{task_description}

Requirements:
- Ensure the code is complete and syntactically correct.
- Include necessary imports.
- Use Pydantic models for data validation.
- Include error handling and docstrings.
- Follow best practices and code style guidelines.

Provide the code only, without additional explanations.
"""

class DatabaseAgent(BaseAgent):
    def create_prompt(self, task_description):
        task_description = self.sanitize_input(task_description)
        return f"""
You are an expert database engineer.

Task:
{task_description}

Requirements:
- Generate SQL code that is complete and syntactically correct.
- Optimize for performance and security.
- Include comments explaining complex parts of the query.
- Follow best practices.

Provide the SQL code only, without additional explanations.
"""

class TaskDecomposer(BaseAgent):
    def create_prompt(self, project_description):
        project_description = self.sanitize_input(project_description)
        return f"""
As an expert project manager and software architect, analyze the following project description and break it down into specific, actionable tasks for frontend, backend, and database development.

Project Description:
{project_description}

Requirements:
- For each task, provide a brief description.
- Specify which type of agent ('frontend', 'backend', or 'database') should handle it.
- Output the tasks in valid JSON format.

Example Output:
[
  {{"type": "frontend", "task": "Implement the login page"}},
  {{"type": "backend", "task": "Set up user authentication endpoints"}},
  ...
]
"""

    def decompose_project(self, project_description):
        prompt = self.create_prompt(project_description)
        response = self.generate_ensemble_response(prompt)
        try:
            tasks = json.loads(response)
            return tasks
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON from task decomposition: {e}")
            raise

class CodeReviewer(BaseAgent):
    def create_prompt(self, code, language):
        code = self.sanitize_input(code)
        return f"""
As an expert {language} developer, review the following code and suggest improvements.

Code:
{code}

Requirements:
- Focus on code quality, efficiency, and adherence to best practices.
- Provide suggestions in a clear, actionable format.
- Do not include the original code in your response.

Output Format:
1. Brief description of issue or improvement.
   - Suggestion: Specific suggestion for improvement.
2. Next issue or improvement.
   - Suggestion: Next suggestion.
...
"""

    def review_code(self, code, language):
        prompt = self.create_prompt(code, language)
        return self.generate_ensemble_response(prompt)

class CodeEvaluator(BaseAgent):
    def create_prompt(self, code, task_description, success_metric):
        code = self.sanitize_input(code)
        task_description = self.sanitize_input(task_description)
        success_metric = self.sanitize_input(success_metric)
        return f"""
Evaluate the following code based on how well it accomplishes the described task and the given success metric.

Task:
{task_description}

Success Metric:
{success_metric}

Code:
{code}

Requirements:
- Provide a score from 1 to 10.
- Include a brief explanation for the score.
- Do not include the original code in your response.

Output Format:
Score: [1-10]
Explanation: [Brief explanation of the score]
"""

    def evaluate_code(self, code, task_description, success_metric):
        prompt = self.create_prompt(code, task_description, success_metric)
        return self.generate_ensemble_response(prompt)

class TestGenerator(BaseAgent):
    def create_prompt(self, code, language):
        code = self.sanitize_input(code)
        return f"""
As an expert in test-driven development, generate comprehensive unit tests for the following {language} code.

Code:
{code}

Requirements:
- Cover all major functionalities and edge cases.
- Use the appropriate testing framework for {language}.
- Provide the test code only, without additional explanations.
"""

    def generate_tests(self, code, language):
        prompt = self.create_prompt(code, language)
        return self.generate_ensemble_response(prompt)

class GameDevelopmentAgent(BaseAgent):
    def create_prompt(self, task_description):
        task_description = self.sanitize_input(task_description)
        return f"""
        You are an expert Python game developer experienced with Pygame.

        Task:
        {task_description}

        Requirements:
        - Use Pygame for graphics and handling user input.
        - Ensure the code is complete, syntactically correct, and runs without errors.
        - Include necessary imports and initialization code.
        - Follow best practices and code style guidelines.
        - Provide comments explaining key parts of the code.

        Provide the full code only, without additional explanations.
        """
        
        def generate_code(self, task_description):
            return super().generate_code(task_description)