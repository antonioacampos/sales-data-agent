#!/usr/bin/env python3
import os
import argparse
import anthropic
from data_loader import load_sales_data, calculate_summary, format_data_for_agent

SYSTEM_PROMPT = """You are an Executive Sales Intelligence Agent. Focus on:
1. ANALYZE sales data objectively
2. IDENTIFY patterns and anomalies
3. EXTRACT actionable insights
4. COMMUNICATE in executive language"""

def run_agent(data_context: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

    user_message = f"Analyze this sales data and generate an executive intelligence report.\n\n{data_context}"

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}]
    )
    return message.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Sales Data Intelligence Agent")
    parser.add_argument('--data', type=str, help='Path to CSV file')
    parser.add_argument('--output', type=str, help='Output report path')
    parser.add_argument('--demo', action='store_true', help='Run with sample data')

    args = parser.parse_args()
    print("Agent configured and ready.")

if __name__ == "__main__":
    main()
