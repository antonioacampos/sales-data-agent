#!/usr/bin/env python3
import os
import argparse
import anthropic

SYSTEM_PROMPT = """You are an Executive Sales Intelligence Agent. Your role is to:

1. ANALYZE the provided sales data objectively
2. IDENTIFY patterns, trends, and anomalies
3. EXTRACT actionable insights for business leaders
4. COMMUNICATE findings in clear, executive-friendly language

OUTPUT FORMAT:
- Executive Summary (1-2 sentences of key finding)
- Top 3 Insights (with context)
- Risks Identified
- Recommended Next Actions (3-5 concrete steps)
- Confidence Level"""

def run_agent(data_context: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": data_context}]
    )
    return message.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Sales Data Intelligence Agent")
    parser.add_argument('--data', type=str, help='Path to CSV file')
    parser.add_argument('--output', type=str, help='Output report path')
    parser.add_argument('--demo', action='store_true', help='Run with sample data')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
