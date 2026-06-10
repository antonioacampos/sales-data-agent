#!/usr/bin/env python3
import os
import sys
import argparse
import anthropic
from pathlib import Path
from data_loader import load_sales_data, create_sample_data, calculate_summary, format_data_for_agent
from report import generate_report

SYSTEM_PROMPT = """You are an Executive Sales Intelligence Agent. Focus on actionable insights for business leaders."""

def run_agent(data_context: str) -> str:
    try:
        client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        if not os.environ.get('ANTHROPIC_API_KEY'):
            raise ValueError("ANTHROPIC_API_KEY not set")

        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": f"Analyze this: {data_context}"}]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        raise

def main():
    parser = argparse.ArgumentParser(description="Sales Data Intelligence Agent")
    parser.add_argument('--data', type=str, default=None)
    parser.add_argument('--output', type=str, default=None)
    parser.add_argument('--demo', action='store_true')

    args = parser.parse_args()

    try:
        data_file = args.data
        if args.demo or not data_file:
            data_file = create_sample_data()

        if not Path(data_file).exists():
            raise FileNotFoundError(f"Data file not found: {data_file}")

        data = load_sales_data(data_file)
        if not data:
            raise ValueError("No data found in file")

        summary = calculate_summary(data)
        context = format_data_for_agent({'summary': summary})

        output = run_agent(context)
        report = generate_report(output, args.output)
        print(report)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
