#!/usr/bin/env python3
import os
import anthropic

def run_agent(data_context: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": data_context}]
    )
    return message.content[0].text
