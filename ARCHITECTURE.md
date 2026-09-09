# How it works

Three modules, no framework. CSV in, markdown out.

```
data_loader.py  ->  agent.py  ->  report.py
```

## data_loader.py

Reads the CSV with csv.DictReader and walks the rows once to build the totals.
format_data_for_agent() turns those totals into the block that goes to the model.
Also holds the sample dataset behind --demo.

## agent.py

The system prompt, one API call, and the CLI entry point. Everything that can go
wrong before the call (no key, no file, empty file) prints to stderr and exits 1.

The call goes to DeepSeek through the OpenAI SDK, pointed at
https://api.deepseek.com. Swapping backends means changing the client and the
model name, nothing else.

## report.py

Wraps whatever the model returned with a header and a timestamp, and writes it to
disk when --output is given.

## Notes

The raw rows never leave the machine. Only the summary block is sent, so the
request stays small no matter how big the export gets.
