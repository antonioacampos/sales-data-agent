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
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Analyze this sales data: {data_context}"}]
    )
    return message.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Sales Data Intelligence Agent")
    parser.add_argument('--data', type=str, default=None, help='Path to CSV file')
    parser.add_argument('--output', type=str, default=None, help='Output report path')
    parser.add_argument('--demo', action='store_true', help='Run with sample data')

    args = parser.parse_args()

    data_file = args.data
    if args.demo or not data_file:
        data_file = create_sample_data()

    data = load_sales_data(data_file)
    summary = calculate_summary(data)
    context = format_data_for_agent({'summary': summary, 'data': data})

    output = run_agent(context)
    report = generate_report(output, args.output)
    print(report)

if __name__ == "__main__":
    main()
