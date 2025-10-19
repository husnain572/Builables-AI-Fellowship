
# Week 2 Assignment: Conversational LLM Interface

## Overview
This project demonstrates the implementation of a **conversational LLM interface** using OpenAI’s GPT models.  
It includes:

- A **CLI-based chat interface**  
- A **Streamlit web interface**  
- Multiple **system prompt personas** (Professional, Creative, Technical)  
- **Conversation persistence** using local JSON files  
- **Prompt engineering experimentation** with different response styles

The goal is to explore **prompt engineering**, maintain conversation context, and provide a functional interface for AI-powered chat.

## Features

1. **Multiple Personas**
   - **Professional:** Formal, business-like tone  
   - **Creative:** Imaginative and storytelling responses  
   - **Technical:** Detailed, precise, technical explanations  

2. **Persistent Conversation**
   - Chat history is saved locally in `data/chat_history_<mode>_<timestamp>.json`  
   - Messages are preserved even if the app is closed or refreshed

3. **Streamlit Web Interface**
   - Sidebar to select persona
   - Displays message history
   - Save chat history with timestamped filenames
   - Real-time interaction with GPT-4o-mini

---

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Week_2_ConversationalLLM

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   **Linux / MacOS:**

   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up OpenAI API key

   * Create a `.env` file in the project root:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

### 1. Run Streamlit App

```bash
streamlit run src/streamlit_chat.py
```

* Select a **persona** from the sidebar
* Type your messages and click **Send**
* Save conversation history with **Save Chat** button
* Each saved file includes the persona, system prompt, and full conversation

### 2. CLI Chat (Optional)

```bash
python src/cli_chat.py
```

* Type messages in terminal
* Type `exit` to end the chat


## Project Folder Structure

```
Week_2_ConversationalLLM/
│
├── data/                       # Saved chat histories
│   └── chat_history_<mode>_<timestamp>.json
├── docs/
│   └── screenshots/            # Screenshots of different personas
├── src/
│   ├── streamlit_chat.py       # Streamlit web interface
│   ├── cli_chat.py             # Command-line chat interface
│   └── utils/                  # Helper modules (if any)
├── .env                        # OpenAI API key
├── requirements.txt            # Python dependencies
└── README.md
```

## Example Screenshots
- Screenshots are available in `docs/screenshots` folder.

## Reflection (Prompt Engineering Insights)

In this assignment, I explored **prompt engineering** and how system prompts influence LLM behavior:

1. **Persona-specific Responses:**

   * Changing the system prompt drastically affected response style, tone, and detail level.
   * Professional mode generated concise and formal answers.
   * Creative mode produced imaginative, expressive outputs.
   * Technical mode focused on precise, structured explanations.

2. **Maintaining Context:**

   * Conversation memory via `st.session_state` allowed the AI to reference prior messages, giving coherent multi-turn conversations.

3. **Challenges:**

   * Initially, chat history was being overwritten due to reinitialization of session state.
   * Correct handling of persona changes required updating the system message dynamically and saving the selected persona in JSON.

4. **Key Learning:**

   * Prompt engineering is not just about what you ask but also **how you define the AI persona and conversation context**.
   * Even small tweaks in system prompts can dramatically change outputs.

## Bonus Feature

* **Persistent chat memory across sessions**

  * Saved chat files include timestamp and persona to avoid overwriting
  * Allows review or reload of previous conversations for analysis

## Dependencies

* `streamlit`
* `openai`
* `python-dotenv`
-----