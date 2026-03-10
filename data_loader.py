import csv
from typing import List, Dict

def load_sales_data(filepath: str) -> List[Dict]:
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def calculate_summary(data: List[Dict]) -> Dict:
    total_revenue = sum(float(row.get('revenue', 0)) for row in data)
    num_records = len(data)
    return {
        'total_revenue': total_revenue,
        'num_records': num_records,
        'avg_transaction': total_revenue / num_records if num_records > 0 else 0,
    }
