import os

# Get the absolute path to the dataset directory
DATASET_PATH = os.path.join(os.path.dirname(__file__), 'utils', 'dataset')

# CSV file paths
CSV_FILES = {
    'sellers': os.path.join(DATASET_PATH, 'olist_sellers_dataset.csv'),
    'customers': os.path.join(DATASET_PATH, 'olist_customers_dataset.csv'),
    'orders': os.path.join(DATASET_PATH, 'olist_orders_dataset.csv'),
    'products': os.path.join(DATASET_PATH, 'olist_products_dataset.csv'),
    'order_items': os.path.join(DATASET_PATH, 'olist_order_items_dataset.csv'),
    'order_payments': os.path.join(DATASET_PATH, 'olist_order_payments_dataset.csv'),
    'reviews': os.path.join(DATASET_PATH, 'olist_order_reviews_dataset.csv'),
    'category_translation': os.path.join(DATASET_PATH, 'product_category_name_translation.csv')
}