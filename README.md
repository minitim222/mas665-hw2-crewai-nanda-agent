# 🤖 MAS.665 HW2: Tim's Digital Twin with NANDA Adapter Integration

## 📋 Overview
This project extends my CrewAI digital twin agent from HW1 by integrating it with the NANDA Adapter SDK, enabling Agent-to-Agent (A2A) communication and participation in the global agent network. The agent embodies my skills, personality, and research background as a computational biology graduate student at Harvard University, now enhanced with universal communication capabilities.

## 🤝 AI Usage Disclosure
**Percentage of AI assistance in this project:**
- **NANDA Integration**: ~30% - AI assisted with adapter configuration, debugging connection issues, and understanding A2A protocols
- **Infrastructure Setup**: ~40% - AI helped with AWS EC2 deployment, SSL certificate configuration, and domain setup
- **Documentation**: ~35% - AI assisted with README updates, technical writing, and homework requirement coverage
- **Troubleshooting**: ~45% - AI provided guidance on dependency resolution, Python environment issues, and git repository management

The core agent persona, research background, and CV data remain 100% authentic and human-generated. The original CrewAI implementation from HW1 is preserved, with NANDA integration added as a wrapper layer.

## 🧬 About the Digital Twin Agent
My digital twin represents me (Wuxinhao/Tim Cao) as a computational biology researcher specializing in:
- 🧠 Spatial transcriptomics and neural stem cell biology
- 🤖 Machine learning and deep learning applications in biology
- 🛠️ Development of computational tools for scientific research
- 🔬 Multi-omics data analysis and visualization

## ⚡ Enhanced Agent Capabilities (HW2 Features)
The agent can now:
- 👋 Introduce me professionally to academic and professional audiences
- 🔬 Explain my research on pregnancy-driven neural stem cell niche remodeling
- 💻 Describe my technical skills in Python, R, and spatial omics
- 🎯 Discuss my career goals in computational biology and neuroscience
- **🌐 NEW: Communicate with other agents via A2A protocol**
- **📋 NEW: Register and be discoverable in the global NANDA registry**
- **🔗 NEW: Participate in inter-agent collaborations and conversations**

## 🚀 Technical Architecture

### 🏗️ HW2 Infrastructure Setup
- **☁️ Deployment**: AWS EC2 t3.micro (Amazon Linux 2023)
- **🌐 Domain**: tim-digital-twin.site with SSL certificates
- **🔐 Security**: Let's Encrypt HTTPS configuration
- **📡 Communication**: NANDA Adapter SDK for A2A protocol
- **📋 Registry**: Integrated with global agent discovery system

### 🤖 Agent Framework
- **Base**: CrewAI multi-agent orchestration
- **Wrapper**: NANDA Adapter for universal communication
- **LLM**: Anthropic Claude API
- **Knowledge**: CV-based personal and professional background

## 📦 Installation and Setup

### 📋 Prerequisites
- 🐍 Python 3.10+ (required for MCP dependencies)
- 🔑 Anthropic API key
- ☁️ AWS account for EC2 deployment
- 🌐 Custom domain for agent endpoint

### 🛠️ Local Development Setup
```bash
# Clone the repository
git clone https://github.com/minitim222/mas665-hw2-crewai-nanda-agent.git
cd mas665-hw2-crewai-nanda-agent

# Create virtual environment with Python 3.11
python3.11 -m venv digital_twin_env
source digital_twin_env/bin/activate

# Install dependencies
pip install crewai nanda-adapter anthropic

# Set up environment variables
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# Run the agent locally
python crewai_agent.py
```

### 🌐 Production Deployment
```bash
# On AWS EC2 instance
sudo yum install python3.11 python3.11-pip -y
python3.11 -m venv production_env
source production_env/bin/activate
pip install -r requirements.txt

# Configure SSL certificates
sudo certbot certonly --standalone -d tim-digital-twin.site

# Run agent with NANDA integration
python crewai_agent.py
```

## 🎮 How to Interact with the Agent

### 🔄 Local Execution
When run locally, the agent executes the same tasks as HW1:
1. 👋 **Introduction Task**: Professional self-introduction
2. 🔬 **Research Explanation**: Spatial transcriptomics research details
3. 💪 **Skills Showcase**: Technical capabilities and tools
4. 🎯 **Career Goals**: Future aspirations in computational biology

### 🌐 Network Interaction (NEW)
With NANDA integration, the agent can:
- Register automatically in the global agent registry
- Be discovered by other agents for collaboration
- Respond to A2A communication requests
- Participate in multi-agent conversations

## 📄 Sample Agent Output
The agent maintains the same authentic voice and comprehensive responses from HW1, including detailed introductions covering my education at University of Toronto and Harvard, research at Boston Children's Hospital, publications in Nature Neuroscience and Nature Communications, and technical expertise in spatial omics and machine learning.

## ⚙️ MAS.665 HW2 Deliverables Status

### ✅ Tech Track Requirements Met
- **📁 GitHub Repository**: Complete code, configuration, and adapter integration
- **🔌 NANDA Integration**: Agent successfully wrapped with universal adapter layer  
- **📋 Registry Registration**: Agent visible and discoverable in NANDA registry
- **🌐 A2A Communication**: Inter-agent messaging and discovery enabled
- **☁️ AWS Deployment**: Running on EC2 with custom domain and SSL

### 📸 Registry Screenshot Status
Agent successfully registered and visible on the NANDA Registry chat platform, confirming proper adapter setup and integration.

## 💭 Agent Description & NANDA Adapter Feedback

### What This Agent Does
This CrewAI-based digital twin agent learns from my CV and professional background to authentically represent my research expertise and communication style. It ingests information from my resume, work experience at Boston Children's Hospital, education at Harvard and University of Toronto, and publication record to create a conversational agent that can introduce me professionally, explain my spatial transcriptomics research, and discuss my computational biology expertise.

The multi-agent CrewAI framework allows specialized agents to handle different aspects of representation - technical expertise, research communication, and professional networking - creating a nuanced digital twin that can engage authentically across academic and professional contexts.

### NANDA Adapter Integration Experience

**Implementation Success:**
The NANDA Adapter SDK successfully transformed my personal digital twin into a discoverable agent within the global network. The integration required minimal changes to the existing CrewAI implementation, essentially wrapping the agent with universal communication capabilities. Automatic registry registration worked seamlessly, making the agent immediately discoverable for inter-agent collaboration.

**Technical Challenges:**
Primary obstacles were infrastructure-related. Python version compatibility required upgrading from 3.9 to 3.11 to support MCP protocol dependencies. The deployment process involved careful SSL certificate management and domain configuration. Browser port restrictions (port 6000 security warnings) limited direct web access, though the agent functioned correctly via IP address.

**Privacy and Representation Considerations:**
Deploying a personal digital twin raises important questions about authentic representation and data privacy. The agent broadcasts my professional profile and research background to a global network, requiring careful consideration of public versus private information boundaries. The accuracy of representation becomes critical when the digital twin may interact with other agents or potential collaborators autonomously.

**Overall Assessment:**
The NANDA framework enables powerful networking capabilities for digital twins, allowing AI representatives to discover and collaborate with others in the agent ecosystem. The concept of networkable digital twins is compelling for academic and professional applications, though production deployment requires addressing accessibility and security concerns. The adapter succeeds in its core mission of enabling universal agent communication while highlighting areas where infrastructure tooling could be streamlined.

## 📊 What I Learned (Building on HW1)

### ✅ What Worked Well
- 🎉 NANDA integration preserved existing CrewAI functionality
- 🤖 Agent maintained authentic voice and comprehensive knowledge
- 🌐 Registry registration and discovery worked automatically
- 🔐 SSL and domain configuration provided production-ready deployment
- 📡 A2A communication protocols functioned as designed

### ⚠️ Challenges Encountered
- 🐍 Python version compatibility issues (required 3.10+)
- 🌐 Browser security restrictions on non-standard ports
- 📦 Complex dependency resolution for MCP protocols
- 🔐 SSL certificate management and domain propagation timing
- 🔧 Infrastructure setup complexity for production deployment

### 🎓 Key Learnings
- 🌍 Understanding of agent networking and discovery protocols
- 🔌 Experience with universal adapter patterns for AI systems
- ☁️ AWS deployment and domain management skills
- 🤝 Insights into distributed agent system architectures
- 📋 Registry-based service discovery implementation

## 📁 Project Structure
```
digital_twin_like/
├── crewai_agent.py          # Main agent with NANDA integration
├── src/                     # CrewAI source modules
│   └── digital_twin_like/
│       ├── config/
│       │   ├── agents.yaml  # Agent configuration
│       │   └── tasks.yaml   # Task definitions
│       └── crew.py          # Crew orchestration
├── knowledge/               # CV and background data
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🛠️ Technologies Used
- 🤖 **CrewAI**: Multi-agent orchestration framework (from HW1)
- 🔌 **NANDA Adapter**: Universal A2A communication layer (NEW)
- 🧠 **Anthropic Claude**: Language model for agent responses
- ☁️ **AWS EC2**: Production deployment infrastructure (NEW)
- 🔐 **Let's Encrypt**: SSL certificate management (NEW)
- 🌐 **Custom Domain**: Professional endpoint configuration (NEW)

## 📞 Contact
- 👤 **Name**: Wuxinhao (Tim) Cao
- 📧 **Email**: tim_cao@hsph.harvard.edu
- 🏛️ **Institution**: Harvard T.H. Chan School of Public Health
- 🎓 **Program**: MS in Computational Biology and Quantitative Genetics
- 🔗 **Agent URL**: https://tim-digital-twin.site
