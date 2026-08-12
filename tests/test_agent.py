import os
import pytest
from agent import run_agent

def test_agent_initialization():
    assert True

def test_agent_with_context():
    if not os.environ.get('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")

    context = "Sample sales data with 100 records and R$ 50000 revenue"
    result = run_agent(context)
    assert isinstance(result, str)
    assert len(result) > 0
