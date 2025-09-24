#!/usr/bin/env python3
import os   # <---- ADD THIS, otherwise os.getenv() will fail

from nanda_adapter import NANDA
from crewai import Agent, Task, Crew
from langchain_anthropic import ChatAnthropic

def create_crewai_improvement():
    llm = ChatAnthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="claude-3-haiku-20240307"
    )
    
    improvement_agent = Agent(
        role="Message Improver",
        goal="Improve message clarity and professionalism",
        backstory="You are an expert communicator.",
        llm=llm
    )
    
    def crewai_improvement(message_text: str) -> str:
        task = Task(
            description=f"Improve this message: {message_text}",
            agent=improvement_agent,
            expected_output="An improved version of the message"
        )
        crew = Crew(agents=[improvement_agent], tasks=[task])
        result = crew.kickoff()
        return str(result)
    
    return crewai_improvement


def main():
    nanda = NANDA(create_crewai_improvement())
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    domain = os.getenv("DOMAIN_NAME")
    nanda.start_server_api(anthropic_key, domain)


if __name__ == "__main__":
    main()
