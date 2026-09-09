# sales-data-agent

Takes a sales CSV export and writes an executive summary of it. The file is
aggregated locally into a small context block, and only that block goes to the
model.

## What it does

- loads any CSV with date/product/region/revenue/quantity columns
- summarizes before calling the API, so the request stays the same size as the file grows
- markdown report to stdout, or to a file with --output
- usable as a CLI or imported as a module

## Quick start

```bash
pip install -r requirements.txt
export DEEPSEEK_API_KEY=...
python agent.py --demo
```

## Usage

```bash
python agent.py --data sales.csv --output report.md
```

## Backend

Started on Claude through the Anthropic SDK. Moved to DeepSeek in September 2026
- the context block is small, and DeepSeek is much cheaper per token for this
kind of workload. The call is OpenAI-compatible, see run_agent() in agent.py.

## Docs

- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [examples.py](examples.py)

## Requirements

Python 3.10+ and a DeepSeek API key.

## License

MIT
