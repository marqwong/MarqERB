# Script modified by Marq Wong
# Date: [添加日期]
# Description: This script populates PostgreSQL tables with dummy data and exports the data to CSV files.

import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
import csv
import os

# Create Faker instance
fake = Faker()

# Database connection configuration
DB_CONFIG = {
    'dbname': 'testdb5',
    'user': 'postgres',
    'password': '5678',
    'host': 'localhost',
    'port': '5432'
}

# Function to connect to the database
def connect_db():
    # Modified by Marq Wong
    return psycopg2.connect(**DB_CONFIG)

# Insert dummy data into auth_group table
def populate_auth_group(cursor):
    # Modified by Marq Wong
    cursor.execute('TRUNCATE TABLE auth_group CASCADE')  # Clear the table
    for _ in range(20):
        name = fake.word() + " Group"  # Generate a random group name
        cursor.execute('INSERT INTO auth_group (name) VALUES (%s)', (name,))
    print("Successfully inserted 20 dummy group records! (present by Marq Wong)")

# Insert dummy data into realtors_realtor table
def populate_realtors_realtor(cursor):
    # Modified by Marq Wong
    cursor.execute('TRUNCATE TABLE realtors_realtor CASCADE')  # Clear the table
    for _ in range(20):
        name = fake.name()  # Generate a random name
        photo = f'photos/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/fake_photo_{random.randint(1, 100)}.jpg'  # Simulate a photo path
        description = fake.text(max_nb_chars=500)  # Generate a random description
        phone = fake.numerify(text='+###########')  # Generate a random phone number
        email = fake.email()  # Generate a random email
        is_mvp = random.choice([True, False])  # Randomly assign MVP status
        hire_date = fake.date_time_between(start_date='-5y', end_date='now')  # Generate a random hire date
        cursor.execute('''
            INSERT INTO realtors_realtor (name, photo, description, phone, email, is_mvp, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (name, photo, description, phone, email, is_mvp, hire_date))
    print("Successfully inserted 20 dummy realtor records! (present by Marq Wong)")

# Insert dummy data into contacts_contact table
def populate_contacts_contact(cursor):
    # Modified by Marq Wong
    cursor.execute('TRUNCATE TABLE contacts_contact CASCADE')  # Clear the table
    for _ in range(20):
        listing = fake.sentence(nb_words=4)  # Generate a random listing name
        listing_id = random.randint(1, 100)  # Generate a random listing ID
        name = fake.name()  # Generate a random name
        email = fake.email()  # Generate a random email
        phone = fake.numerify(text='+###########')  # Generate a random phone number
        message = fake.text(max_nb_chars=200)  # Generate a random message
        contact_date = fake.date_time_between(start_date='-1y', end_date='now')  # Generate a random contact date
        user_id = random.randint(1, 20)  # Generate a random user ID
        reservation_date = fake.date_time_between(start_date='now', end_date='+1y') if random.choice([True, False]) else None  # Generate a random reservation date
        cursor.execute('''
            INSERT INTO contacts_contact (listing, listing_id, name, email, phone, message, contact_date, user_id, reservation_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (listing, listing_id, name, email, phone, message, contact_date, user_id, reservation_date))
    print("Successfully inserted 20 dummy contact records! (present by Marq Wong)")

# Export table data to CSV
def export_table_to_csv(cursor, table_name, filename):
    # Modified by Marq Wong
    try:
        cursor.execute(f'SELECT * FROM {table_name}')  # Query table data
        rows = cursor.fetchall()  # Fetch all rows
        filepath = os.path.abspath(filename)  # Get the absolute path of the file
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write the header
            csvwriter.writerow([desc[0] for desc in cursor.description])
            # Write the rows
            csvwriter.writerows(rows)
        print(f"Data from table {table_name} has been exported to {filepath}")  # 路径说明部分不加备注
    except Exception as e:
        print(f"Error exporting data from table {table_name}: {e}")

# Main function
def main():
    # Modified by Marq Wong
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Insert dummy data into tables
        populate_auth_group(cursor)
        populate_realtors_realtor(cursor)
        populate_contacts_contact(cursor)

        # Export table data to CSV
        export_table_to_csv(cursor, 'auth_group', 'auth_group.csv')
        export_table_to_csv(cursor, 'realtors_realtor', 'realtors_realtor.csv')
        export_table_to_csv(cursor, 'contacts_contact', 'contacts_contact.csv')

        # Commit changes
        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()