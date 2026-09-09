# Usage examples

Demo run. Writes sample_sales_data.csv into the cwd first:

```bash
python agent.py --demo
```

Your own export:

```bash
python agent.py --data sales.csv --output report.md
```

As a module, if you want the pieces instead of the CLI:

```python
from data_loader import load_sales_data, calculate_summary, format_data_for_agent
from agent import run_agent

summary = calculate_summary(load_sales_data("sales.csv"))
report = run_agent(format_data_for_agent({"summary": summary}))
```

Weekly run, mondays at 8. cron does not read your shell profile, so the key has
to be exported in the crontab line itself:

```bash
0 8 * * 1 . /etc/sales-agent.env; cd /srv/sales-agent && python agent.py --data weekly.csv --output report.md
```

When it fails:

- `DEEPSEEK_API_KEY not set` - the key is not in the environment, see .env.example
- `Data file not found` - paths are relative to the cwd
- `No data found in file` - the CSV has a header but no rows
