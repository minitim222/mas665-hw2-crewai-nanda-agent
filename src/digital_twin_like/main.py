#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from digital_twin_like.crew import DigitalTwinLike

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew - for the assignment, just run introduction task
    """
    
    print("=== Tim's Digital Twin Introduction ===")
    
    # Simple inputs - can be empty for basic introduction
    inputs = {}
    
    result = DigitalTwinLike().crew().kickoff(inputs=inputs)
    print("Digital Twin Output:")
    print(result)
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    run()