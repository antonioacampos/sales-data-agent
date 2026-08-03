import tempfile
from pathlib import Path
from data_loader import load_sales_data, calculate_summary

def test_load_sales_data():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("date,product,revenue\n")
        f.write("2024-01-01,Product A,1000\n")
        f.flush()

        data = load_sales_data(f.name)
        assert len(data) == 1
        assert data[0]['product'] == 'Product A'

    Path(f.name).unlink()

def test_calculate_summary():
    data = [
        {'revenue': '1000', 'quantity': '10'},
        {'revenue': '2000', 'quantity': '20'},
    ]
    summary = calculate_summary(data)
    assert summary['total_revenue'] == 3000
    assert summary['num_records'] == 2

def test_calculate_summary_skips_unparsable_rows():
    data = [
        {'revenue': 'abc', 'quantity': 'x'},
        {'revenue': '2000', 'quantity': '20'},
    ]
    summary = calculate_summary(data)
    assert summary['total_revenue'] == 2000
    assert summary['total_quantity'] == 20
    assert summary['num_records'] == 2
