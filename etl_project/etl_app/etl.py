import csv
from .models import SalesData

def extract(file_path):
    """
    Extracts data from the provided CSV file.
    This function reads the CSV file and returns a list of dictionaries where each row
    represents a dictionary with column names as keys.
    """
    rows = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def transform(rows):
    """
    Transforms the extracted data by converting strings to the appropriate data types.
    For example, converting 'quantity' to integer and 'price' to float.
    """
    for row in rows:
        try:
            row['quantity'] = int(row['quantity'])  # Convert quantity to integer
            row['price'] = float(row['price'])  # Convert price to float
        except ValueError as e:
            # Handle errors gracefully (e.g., skipping the row if the conversion fails)
            print(f"Error transforming row {row}: {e}")
            continue  # Skip this row if it cannot be transformed
    return rows

def load(rows):
    """
    Loads the transformed data into the database using Django models.
    It creates and saves instances of the SalesData model for each row in the list.
    """
    for row in rows:
        try:
            # Create and save SalesData instances
            sales_data = SalesData(
                date=row['date'],
                product=row['product'],
                quantity=row['quantity'],
                price=row['price']
            )
            sales_data.save()  # Save the instance to the database
        except Exception as e:
            # Log any errors that occur during the loading process
            print(f"Error loading row {row}: {e}")

def run_etl(file_path):
    """
    Runs the full ETL process: Extract, Transform, Load.
    This function coordinates the extract, transform, and load steps.
    """
    rows = extract(file_path)  # Step 1: Extract data from the CSV file
    transformed_rows = transform(rows)  # Step 2: Transform the extracted data
    load(transformed_rows)  # Step 3: Load the transformed data into the database

def process_csv(row):
    # Implement your logic here to process each row of the CSV
    print(row)  # This is just a placeholder for actual processing

