# Tim's Digital Twin - CrewAI Agent

## Overview
This project creates a CrewAI agent that embodies my skills, personality, and research background as a computational biology graduate student at Harvard University.

## About the Agent
My digital twin represents me (Tim Cao) as a computational biology researcher specializing in:
- Spatial transcriptomics and neural stem cell biology
- Machine learning and deep learning applications in biology
- Development of computational tools for scientific research
- Multi-omics data analysis and visualization

## Agent Capabilities
The agent can:
- Introduce me professionally to academic and professional audiences
- Explain my research on pregnancy-driven neural stem cell niche remodeling
- Describe my technical skills in Python, R, and spatial omics
- Discuss my career goals in computational biology and neuroscience

## Technical Implementation

### Agent Configuration
- **Role**: Computational Biology Researcher and Data Science Graduate Student
- **Goal**: Authentically represent Tim Cao's expertise and background
- **Backstory**: Comprehensive background including education at University of Toronto and Harvard, research at Boston Children's Hospital, publications, and technical skills

### Key Tasks
1. **Introduction Task**: Professional self-introduction
2. **Research Explanation**: Detailed explanation of spatial transcriptomics research
3. **Skills Showcase**: Technical abilities and tools developed
4. **Career Goals**: Future aspirations in computational biology

## Setup and Installation

### Prerequisites
- Python 3.10+
- OpenAI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/digital_twin_like.git
cd digital_twin_like

# Install CrewAI
pip install crewai

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env

# Install dependencies
crewai install

# Run the agent
crewai run
```

## Project Structure
```
digital_twin_like/
├── src/
│   └── digital_twin_like/
│       ├── config/
│       │   ├── agents.yaml      # Agent configuration
│       │   └── tasks.yaml       # Task definitions
│       ├── crew.py              # Crew orchestration
│       └── main.py              # Execution entry point
├── .env                         # Environment variables (not in repo)
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Assignment Requirements Met

### ✅ What Worked
- Successfully installed CrewAI and set up project structure
- Configured agent with authentic personal background from CV
- Defined multiple tasks that showcase different aspects of expertise
- Agent successfully executes and provides detailed, authentic responses
- Created reproducible setup with proper configuration management

### ✅ What Didn't Work (Initially)
- Initial API quota limitations with OpenAI (resolved by setting up proper billing)
- Naming mismatches between configuration files (fixed through careful alignment)

### ✅ What I Learned
- How to structure CrewAI agents with personal knowledge and expertise
- The importance of consistent naming across YAML configuration files
- How to create authentic agent personas using real CV data
- The power of CrewAI's configuration-driven approach for rapid prototyping
- Best practices for managing API keys and environment variables

## Sample Output
The agent produces professional, detailed responses that accurately reflect my background in computational biology, spatial transcriptomics research at Boston Children's Hospital, and technical expertise in Python, R, and machine learning.

## Future Enhancements
- Add web search capabilities for current research updates
- Integrate with academic databases for publication queries
- Add file processing tools for CV analysis
- Implement memory for conversation context

## Technologies Used
- **CrewAI**: Multi-agent orchestration framework
- **OpenAI GPT**: Language model for agent responses
- **Python**: Primary programming language
- **YAML**: Configuration management

## Contact
- **Name**: Wuxinhao (Tim) Cao
- **Email**: tim_cao@hsph.harvard.edu
- **Institution**: Harvard T.H. Chan School of Public Health
- **Program**: MS in Computational Biology and Quantitative Genetics