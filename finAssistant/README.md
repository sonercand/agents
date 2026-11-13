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