# 06 - Orchestration with SAP Generative AI Hub

This exercise is a **conceptual / configuration exercise** that you complete in the
SAP Generative AI Hub on SAP BTP, not in this local repository.

It is based on the SAP Developers tutorial:

- **Leveraging Orchestration Capabilities to Enhance Responses**  
  <https://developers.sap.com/tutorials/ai-core-orchestration-consumption-opt.html>

## Goal

Learn how to use **orchestration** in SAP AI Core / Gen AI Hub to enhance
LLM responses with:

- **Data masking** – protect personal or confidential data before it reaches the model.
- **Translation** – handle multilingual inputs and outputs within the orchestration flow.
- **Content filtering** – filter or block unsafe / non‑compliant input and output.

You will design and run an orchestration pipeline (for example, a
sentiment‑analysis use case) that:

- Calls GenAI models via the **harmonized orchestration API**.
- Applies data masking and content filtering modules.
- Optionally adds translation to support multiple languages.

## What you do in this step

In the SAP tutorial (AI Launchpad / SDK / Bruno clients), you will:

- Reuse an existing orchestration deployment in SAP AI Core.
- Configure orchestration modules for data masking, translation, and content filtering.
- Execute the orchestration workflow and inspect the filtered, masked responses.

This repo does **not** contain code for this exercise; it simply documents that
`06` in the Day 2 flow is the **orchestration capabilities** tutorial on SAP BTP.
