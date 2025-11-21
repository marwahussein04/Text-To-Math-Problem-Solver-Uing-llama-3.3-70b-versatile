# 🧮 AI Math Problem Solver & Data Search Assistant

This is a Streamlit application that utilizes a powerful Large Language Model (LLM) integrated with LangChain Agents and tools to solve complex mathematical word problems and perform Wikipedia searches. The project aims to provide accurate, step-by-step solutions by delegating math computations to a specialized tool.

## ✨ Key Features

* **Intelligent Agent:** Uses a `ZERO_SHOT_REACT_DESCRIPTION` Agent to decide whether to use a calculator, search tool, or reasoning tool.
* **Accurate Math Solving:** Delegates complex arithmetic and expressions to the **`Calculator`** tool via the `LLMMathChain` for guaranteed numerical accuracy.
* **Knowledge Retrieval:** Employs the **`Wikipedia`** tool to fetch real-time information relevant to the user's question.
* **Structured Reasoning:** Uses a custom **`Reasoning Tool`** to force the LLM to output a detailed, point-wise explanation of the solution.
* **High Performance:** Powered by the speed of the **Groq API** (using the `llama-3.1-70b-versatile` model or similar fast LLMs).

## 💻 Tech Stack

* **Frontend:** Streamlit
* **LLM Provider:** Groq
* **Framework:** LangChain (`langchain-classic`, `langchain-groq`, `langchain-community`)
* **Core Tools:** `LLMMathChain`, `WikipediaAPIWrapper`

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

You need **Python 3.10+** and a **Groq API Key**.

### 2. Clone the Repository

```bash
git clone [https://github.com/marwahussein04/Text-To-Math-Problem-Solver-Uing-llama-3.3-70b-versatile.git](https://github.com/marwahussein04/Text-To-Math-Problem-Solver-Uing-llama-3.3-70b-versatile.git)
cd Text-To-Math-Problem-Solver-Uing-llama-3.3-70b-versatile
