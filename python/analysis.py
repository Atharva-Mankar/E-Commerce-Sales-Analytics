"""E-commerce customer and sales analytics using the Madhav Kaggle dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE / 'data'
OUT = BASE / 'outputs'
OUT.mkdir(exist_ok=True)

orders = pd.read_csv(DATA / 'Orders.csv')
details = pd.read_csv(DATA / 'Details.csv')
print('Orders:', orders.shape, '| Details:', details.shape)
print('Missing values:', orders.isna().sum().sum() + details.isna().sum().sum())
print('Duplicate rows:', orders.duplicated().sum() + details.duplicated().sum())

orders = orders.drop_duplicates().dropna(subset=['Order ID', 'Order Date'])
details = details.drop_duplicates().dropna(subset=['Order ID', 'Amount', 'Profit'])
orders['Order Date'] = pd.to_datetime(orders['Order Date'], format='%d-%m-%Y', errors='coerce')
orders = orders.dropna(subset=['Order Date'])

sales = details.merge(orders, on='Order ID', how='inner', validate='many_to_one')
sales['Month'] = sales['Order Date'].dt.to_period('M').astype(str)
sales.to_csv(OUT / 'cleaned_ecommerce_sales.csv', index=False)

kpis = pd.Series({
    'Total Sales': sales['Amount'].sum(),
    'Total Profit': sales['Profit'].sum(),
    'Total Orders': sales['Order ID'].nunique(),
    'Total Customers (distinct names)': sales['CustomerName'].nunique(),
    'Total Quantity': sales['Quantity'].sum(),
    'Average Order Value': sales['Amount'].sum() / sales['Order ID'].nunique(),
    'Profit Margin (%)': 100 * sales['Profit'].sum() / sales['Amount'].sum(),
})
print('\nKPIs:\n', kpis.round(2).to_string())
kpis.rename_axis('Metric').reset_index(name='Value').to_csv(OUT / 'kpis.csv', index=False)

reports = {
    'monthly_sales': sales.groupby('Month', as_index=False)[['Amount', 'Profit']].sum(),
    'category_sales': sales.groupby('Category', as_index=False)[['Amount', 'Profit']].sum().sort_values('Amount', ascending=False),
    'state_sales': sales.groupby('State', as_index=False)[['Amount', 'Profit']].sum().sort_values('Amount', ascending=False),
    'top_customers': sales.groupby('CustomerName', as_index=False)['Amount'].sum().sort_values('Amount', ascending=False).head(10),
    'payment_modes': sales.groupby('PaymentMode', as_index=False)['Amount'].sum().sort_values('Amount', ascending=False),
    'subcategory_sales': sales.groupby('Sub-Category', as_index=False)[['Amount', 'Profit']].sum().sort_values('Amount', ascending=False),
}
for name, frame in reports.items():
    frame.to_csv(OUT / f'{name}.csv', index=False)
    print(f'\n{name}:\n', frame.head(10).to_string(index=False))

plots = [
    ('monthly_sales', 'Month', 'Amount', 'Monthly Sales', 'monthly_sales.png'),
    ('category_sales', 'Category', 'Amount', 'Sales by Category', 'category_sales.png'),
    ('state_sales', 'State', 'Amount', 'Top 10 States by Sales', 'top_states.png'),
    ('payment_modes', 'PaymentMode', 'Amount', 'Sales by Payment Mode', 'payment_modes.png'),
]
for key, x, y, title, filename in plots:
    frame = reports[key].head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(frame[x], frame[y])
    ax.set(title=title, ylabel='Sales Amount', xlabel=x)
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=160)
    plt.close(fig)
print('\nSaved cleaned data, reports and charts to outputs/.')
