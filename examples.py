def example_basic_usage():
    from agent import main
    import sys
    sys.argv = ['agent.py', '--demo']
    main()

def example_with_custom_data():
    from agent import run_agent
    from data_loader import load_sales_data, format_data_for_agent

    data = load_sales_data("my_sales.csv")
    context = format_data_for_agent({"summary": {}, "data": data})
    report = run_agent(context)
    return report

def example_generate_report():
    from agent import run_agent
    from report import generate_report

    context = "Sales data here..."
    output = run_agent(context)
    report = generate_report(output, "output.md")
