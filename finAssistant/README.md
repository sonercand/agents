# Financial Assistant with Web Search (Google ADK)

A modular multi-agent financial assistant built using the Google Agent Development Kit (ADK), Pydantic for structured data validation, and custom Python math utilities.

## Architecture Overview

- **`financial_assistant_agent` (Root Agent)** (`agent.py`): Orchestrates user queries, delegating web searches to sub-agents and calculations to Python tools.
- **`structured_search_agent`** (`search_agent.py`): Wraps Google Search and enforces a strict Pydantic output schema (`StockSearchResult`) to guarantee type-safe data.
- **`search_agent_tool`**: An `AgentTool` wrapper that allows the root agent to call the search sub-agent like a standard function.
- **Custom Math Tools** (`tools.py`): Deterministic Python functions for calculating percentage changes and profit/loss.

## File Structure

```text
├── tools.py             # Deterministic calculation functions
├── search-prompt.txt    # System instructions for the search sub-agent
├── search_agent.py      # Search sub-agent and Pydantic schema definition
├── agent-prompt.txt     # System instructions for the root orchestrator
└── agent.py             # Root financial assistant agent configuration


## How to Run

To run the application, open three separate terminal windows and execute the following commands in order:

### 1. Start Cloud SQL Auth Proxy
Establish a secure local tunnel to your Cloud SQL instance:
```bash
./cloud-sql-proxy YOUR_PROJECT_ID:YOUR_REGION:YOUR_INSTANCE_NAME --port 3306

### 2. mcp toolbox
./toolbox --config dbAssistant/tools.yaml --port 5001
### 3. 
TOOLBOX_URL=[http://127.0.0.1:5001](http://127.0.0.1:5001) GOOGLE_GENAI_USE_VERTEXAI=true GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID GOOGLE_CLOUD_LOCATION=global adk web 