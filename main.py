# main.py

import argparse
from orchestrator import Orchestrator
import time
import logging

def main():
    parser = argparse.ArgumentParser(description="Agentic AI Framework for Code Generation")
    parser.add_argument("--description", type=str, help="Project description")
    parser.add_argument("--load", type=str, help="Load project state from file")
    args = parser.parse_args()

    orchestrator = Orchestrator()

    if args.load:
        state = orchestrator.load_project_state(args.load)
        logging.info(f"Loaded project state: {state}")
    elif args.description:
        orchestrator.run(args.description)
        orchestrator.save_project_state()
    else:
        print("Please provide either a project description using --description or a state file to load using --load.")
        return

    # Keep the script running to maintain the dashboard
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Shutting down.")

if __name__ == "__main__":
        main()
