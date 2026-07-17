# AI Agency OS

AI Agency OS is a comprehensive, Streamlit-based application designed to orchestrate and manage a suite of specialized AI agents. It serves as a unified dashboard to streamline agency operations, including research, marketing, outreach, and competitor analysis.

## 🚀 Features

The application is modularized into several core pages, each backed by specific AI agents:

- **Dashboard**: A central hub to monitor agent activities and recent modules used.
- **Content Studio / Marketing**: Generate and manage marketing campaigns and content creation.
- **Research**: Conduct deep market research and aggregate news using specialized research agents and search tools (DuckDuckGo, Tavily).
- **Outreach**: Automate and track outreach campaigns and communications.
- **Competitor Analysis**: Analyze competitors' strategies and market positioning.

## 🛠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **AI/Agents**: `openai-agents`
- **Search & Tools**: `duckduckgo-search`, `tavily-python`
- **Package Management**: `uv`

## ⚙️ Setup & Installation

This project uses `uv` for fast dependency management and relies on Python 3.13+.

1. **Clone the repository and navigate to the project directory:**
   ```bash
   cd AI_agency_os
   ```

2. **Create a virtual environment and install dependencies:**
   Using `uv`:
   ```bash
   uv venv
   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   
   uv pip install -r pyproject.toml
   ```
   *(Alternatively, if you are using pip, you can install the dependencies listed in `pyproject.toml`)*

3. **Configure Environment Variables:**
   Create a `.env` file in the root of the `AI_agency_os` directory and add your necessary API keys:
   ```env
   # Example .env configuration
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## 🎯 Usage

To start the AI Agency OS locally, run the following command from the `AI_agency_os` directory:

```bash
streamlit run app.py
```

The application will launch in your default web browser, giving you access to the sidebar navigation to switch between the different AI modules.

## 📁 Project Structure

- `app.py`: The main entry point for the Streamlit application.
- `ai_agents/`: Contains the logic and definitions for various AI agents (research, campaign, outreach, competitor).
- `components/`: Reusable UI components for the Streamlit frontend.
- `pages/`: Individual Streamlit pages mapping to the features.
- `utils/`: Helper utilities and shared functions.
- `prompts/`: (inside `ai_agents/`) System prompts used to guide agent behavior.
