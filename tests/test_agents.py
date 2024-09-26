# tests/test_agents.py

import unittest
from specialized_agents import FrontendAgent, BackendAgent, DatabaseAgent

class TestAgents(unittest.TestCase):
    def test_frontend_agent(self):
        agent = FrontendAgent()
        code = agent.generate_code("Create a React component that displays a greeting message.")
        self.assertIsNotNone(code)
        # Additional assertions can be added

    def test_backend_agent(self):
        agent = BackendAgent()
        code = agent.generate_code("Implement an API endpoint that returns user data.")
        self.assertIsNotNone(code)
        # Additional assertions can be added

    def test_database_agent(self):
        agent = DatabaseAgent()
        code = agent.generate_code("Create a SQL query to retrieve all users over the age of 18.")
        self.assertIsNotNone(code)
        # Additional assertions can be added

if __name__ == '__main__':
    unittest.main()
