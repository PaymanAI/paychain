# Paychain 🔗💰

A sample project to demonstrate how to use the Payman AI payment tools integrated with LangChain.

## Quick Start 🚀

1. Clone the repository:
```bash
git clone <repository-url>
cd paychain-test
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
PAYMAN_API_SECRET=your_payman_api_secret
OPENAI_API_KEY=your_openai_api_key
PAYMAN_ENVIRONMENT=sandbox  # or production
```

5. Run the tests:
```bash
# Test AI agent with all payment tools
python examples/test_agent.py
```

## Features ✨

- Direct payment processing
- AI agent with natural language payment processing
- Multiple payment tools:
  - Send payments
  - Search payees
  - Add new payees
  - Request money
  - Check balances

## Project Structure 📁

```
paychain-examples/
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore file
├── README.md           # This file
├── requirements.txt    # Project dependencies
└── examples/           # Test examples
    ├── __init__.py
    ├── test_payment.py # Basic payment test
    └── test_agent.py   # AI agent test
```

## Security 🔒

- Never commit your `.env` file
- Keep your API keys secure
- Use sandbox environment for testing

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄

MIT 