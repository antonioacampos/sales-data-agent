#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from openai import OpenAI
from data_loader import load_sales_data, create_sample_data, calculate_summary, format_data_for_agent
from report import generate_report

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-flash"

SYSTEM_PROMPT = """You are an Executive Sales Intelligence Agent. Focus on actionable insights for business leaders."""

def run_agent(data_context: str) -> str:
    try:
        api_key = os.environ.get('DEEPSEEK_API_KEY')
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not set")

        client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1500,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analyze this: {data_context}"},
            ],
        )
        return response.choices[0].message.content
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
