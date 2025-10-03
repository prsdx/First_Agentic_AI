# 🤖 AI Research Agent: LangChain-Powered Knowledge Explorer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-green?logo=langchain&logoColor=white)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/yourusername/ai-research-agent?style=social)](https://github.com/yourusername/ai-research-agent)

A beginner-friendly **autonomous AI research assistant** built with **LangChain** and **Google's Gemini** LLM. Inspired by [Tech With Tim's tutorial](https://www.youtube.com/watch?v=bTMPwUgLZf0), this agent researches any topic by querying Wikipedia and the web (via DuckDuckGo), generates structured summaries, and saves results to a file—all while reasoning step-by-step like a pro researcher.

Perfect for prototyping AI agents, learning tool-calling, or automating quick fact-finds. No fluff: Just 200 lines of clean Python that packs a punch.

## ✨ Features

- **Autonomous Agent**: Uses LangChain's `create_tool_calling_agent` with ReAct reasoning (Reason + Act) to decide when to search, summarize, or save.
- **Multi-Tool Integration**:
  - Wikipedia: Fetches and summarizes articles (customizable snippet length).
  - DuckDuckGo Search: Real-time web queries for broader context.
  - File Saver: Appends timestamped, structured outputs to `research_output.txt`.
- **Structured Outputs**: Pydantic models ensure clean JSON-like responses (topic, summary, sources, tools used).
- **Gemini LLM**: Free-tier friendly with Google's fast `gemini-2.5-flash` model—swap to others (OpenAI, Groq) easily.
- **Verbose Logging**: Watch the agent "think" in real-time for debugging or fun.
- **Extensible**: Add memory for conversations or more tools (e.g., math solvers) in minutes.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+.
- A free [Google Gemini API key](https://aistudio.google.com/app/apikey) (no credit card needed; generous free tier).

### Setup
1. **Clone the Repo**:
   ```
   git clone https://github.com/prsdx/First_Agentic_AI
   cd ai-research-agent
   ```

2. **Virtual Environment** (Recommended):
   ```
   python -m venv env
   source env/bin/activate  # macOS/Linux
   # or env\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
   (Or run: `pip install langchain langchain-community langchain-google-genai wikipedia duckduckgo-search python-dotenv pydantic`)

4. **Add Your API Key**:
   Create a `.env` file in the root:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
   (Add `env/` and `.env` to `.gitignore`—sample included.)

### Run It
```
python main.py
```
- Enter a query: e.g., "What are Python virtual environments?"
- Watch the magic: Agent searches, reasons, and outputs a structured summary.
- Check `research_output.txt` for saved results.

## 📁 Code Structure

| File/Section | Description |
|--------------|-------------|
| `agent.py` | Main script: LLM init, tools, prompt, agent executor. Run this! |
| `requirements.txt` | All deps (generated via `pip freeze`). |
| `.env.example` | Template for API keys (copy to `.env`). |
| `.gitignore` | Ignores envs, caches, and secrets. |
| `research_output.txt` | Auto-generated: Timestamped research dumps. |

Key snippets:
- **LLM**: `ChatGoogleGenerativeAI(model="gemini-2.5-flash")`—fast & free.
- **Tools**: Custom `Tool` wrappers for search/save; Wikipedia via `WikipediaQueryRun`.
- **Prompt**: System message guides tool use; Pydantic parser enforces structure.
- **Agent**: `create_tool_calling_agent` + `AgentExecutor` for execution.

## 🎉 Example Usage & Output

**Input Query**: "Research the history of AI agents."

**Console Output** (Verbose Mode):
```
> Entering new AgentExecutor chain...
Thought: I need to research the history of AI agents. I'll start with Wikipedia.
Action: wiki_tool
Action Input: history of AI agents
Observation: [Wikipedia snippet: "An intelligent agent (IA) is an entity that perceives its environment..."]
Thought: Got a good overview. Now, web search for recent developments.
Action: search
Action Input: history of AI agents
Observation: [DuckDuckGo results: Links to papers, timelines...]
Thought: Time to summarize and save.
Action: save_text_to_file
Action Input: {"topic": "History of AI Agents", "summary": "...", ...}
Observation: Data successfully saved to research_output.txt
> Finished chain.
```

**Parsed Response**:
```
--- Parsed Research Response ---
Topic: History of AI Agents
Summary: AI agents trace back to 1950s with early AI like ELIZA... Modern era with LangChain and LLMs.
Sources: https://en.wikipedia.org/wiki/Intelligent_agent, https://arxiv.org/abs/...
Tools Used: wiki_tool, search, save_text_to_file
```

**File Save** (`research_output.txt`):
```
---Research Output ---
Timestamp: 2025-10-04 14:30:00

{'topic': 'History of AI Agents', 'summary': '...', 'sources': [...], 'tools_used': [...]}

```

![Screenshot Placeholder](https://via.placeholder.com/800x400?text=Agent+in+Action)  
*(Add your own screenshot here—e.g., terminal output or parsed result.)*

## 🔧 Customization

- **Swap LLM**: Uncomment imports for OpenAI/Claude/Groq; update `llm = ...`.
- **Add Tools**: Extend `tools` list with LangChain's `@tool` decorator.
- **Memory**: For chats, add `ConversationBufferMemory` to `AgentExecutor`.
- **Rate Limits**: Gemini free tier: ~15 req/min. Monitor via AI Studio dashboard.

## 🤝 Contributing

Fork, tweak, PR! Ideas:
- Integrate RAG for PDF uploads.
- Add voice input/output.
- Support more LLMs (e.g., local Ollama).

Report issues [here](https://github.com/prsdx/First_Agentic_AI/issues).


## 🙏 Credits

- Built on [LangChain](https://github.com/langchain-ai/langchain).
- Tutorial inspo: [Tech With Tim](https://www.youtube.com/watch?v=bTMPwUgLZf0).
- Made with ❤️ by [Your Name](https://github.com/yourusername) using Grok's guidance.

---

⭐ **Star if this sparks your AI journey!** Questions? Open an issue. Let's build smarter agents together. 🚀