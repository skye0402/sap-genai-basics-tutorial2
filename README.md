# Day 2 – GenAI + MCP Workshop Project

This repository contains material for a Day 2 hands‑on session that combines
SAP AI Core / Generative AI Hub with **MCP (Model Context Protocol)** and
**LangGraph**.

The day is structured into two main exercises:

## 06 – Orchestration with SAP Generative AI Hub (BTP)

Folder: `06-orchestration/`

- High‑level, **no local coding** exercise.  
- You follow the SAP Developers tutorial:
  - **Leveraging Orchestration Capabilities to Enhance Responses**  
    <https://developers.sap.com/tutorials/ai-core-orchestration-consumption-opt.html>
- Focus topics:
  - Using **orchestration** in SAP AI Core / GenAI Hub.
  - Applying **data masking**, **translation**, and **content filtering** to
    secure and refine LLM responses.

## 07 – MCP Tutorial: Agentic AI with S/4HANA Product API

Exercise folder: `07-mcp-tutorial/`  
Complete solution: `07-mcp-tutorial-complete/`

You will:

- Build an MCP server exposing tools for:
  - Calculator operations (add, subtract, multiply, divide).
  - S/4HANA Cloud **Product Master API** (documentation + product queries).
- Connect the MCP server to a **LangGraph React Agent** running on SAP AI Core.
- Let the agent automatically choose and call tools to:
  - Answer math questions via calculator tools.
  - Search S/4HANA product data (e.g. "APJ*" products, cat‑related products).

The `07-mcp-tutorial` folder contains the **exercise skeleton**, while
`07-mcp-tutorial-complete` shows one possible **reference solution**.

Refer to each subfolder’s `README.md` for detailed setup and instructions.
