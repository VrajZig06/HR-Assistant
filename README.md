# HR‑Assistant

**HR Assistant for simple English prompts**

This Python-based HR Assistant allows users to interact with HR-related tasks by typing simple English commands. It integrates language models to interpret natural language and perform HR functions like employee queries, policy lookups, and more.

---

## Features

- **Natural Language Commands**: Do HR tasks simply by writing plain English prompts.
- **Modular Python Tools**: Includes modules like `Z_Employee_MCP.py` and `Z_HR_Policy.py` for structured functionality.
- **Quick Testing**: `test.py` offers a sandbox to experiment with commands and tools.

---

## Project Structure

```
├── .gradio/                 # Gradio assets (flagged)
├── EmployeData/             # CSV folder holding employee data
│   └── employeeDetails.csv
├── LLM/                     # Folder for language model integrations
├── HR_Assistance.py         # Main interface script
├── Z_Employee_MCP.py        # Employee-focused functions/tools
├── Z_HR_Policy.py           # HR policy-related tools
├── test.py                  # Interactive testing script
└── requirements.txt         # Dependencies required to run the project
```

---

## Getting Started

### Requirements

Ensure you have:

- Python 3.9+
- A CSV file (e.g. `employeeDetails.csv`) inside the `EmployeData/` folder with proper headers

### Installation

```bash
git clone https://github.com/VrajZig06/HR-Assistant.git
cd HR-Assistant
pip install -r requirements.txt
```

### Usage

Test commands interactively:

```bash
python test.py
```

Launch core functionality:

```bash
python HR_Assistance.py
```

---

## Usage Suggestions

- **Employee Lookup**: Type English queries like `Show me employee 123` or `List employees in Sales department`.
- **Policy Retrieval**: Try phrases like `What’s the leave policy?` or `Show benefits details`.
- **Quick Testing**: Use `test.py` to verify commands and new tools before integrating into the main script.

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/<name>`
3. Commit changes and push
4. Open a Pull Request to propose enhancements

---

## License

Add your license information here once decided.

---

## About

Built by **VrajZig06**, HR Assistant simplifies HR tasks through natural language and modular Python tools—no rigid syntax required.
