import csv
from typing import List, Dict

def load_sales_data(filepath: str) -> List[Dict]:
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def calculate_summary(data: List[Dict]) -> Dict:
    total_revenue = sum(float(row.get('revenue', 0)) for row in data)
    total_quantity = sum(int(row.get('quantity', 0)) for row in data)
    num_records = len(data)
    unique_products = len(set(row.get('product') for row in data))
    unique_regions = len(set(row.get('region') for row in data))

    return {
        'total_revenue': total_revenue,
        'total_quantity': total_quantity,
        'num_records': num_records,
        'unique_products': unique_products,
        'unique_regions': unique_regions,
        'avg_transaction': total_revenue / num_records if num_records > 0 else 0,
    }

def format_data_for_agent(data: dict) -> str:
    summary = data['summary']
    context = f"""
SALES DATA SUMMARY:
- Records: {summary['num_records']}
- Total Revenue: R$ {summary['total_revenue']:,.0f}
- Total Quantity: {summary['total_quantity']}
- Unique Products: {summary['unique_products']}
- Unique Regions: {summary['unique_regions']}
"""
    return context
