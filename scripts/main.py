from scripts.database import insert_transaction, fetch_transactions

def run():
    print("Inserting sample transactions...")
    insert_transaction("Bob", 200.00)
    insert_transaction("Charlie", 150.75)
    
    print("Fetching transactions...")
    data = fetch_transactions()
    for row in data:
        print(row)

if __name__ == "__main__":
    run()
