"""
Simulates multiple clients by splitting dataset.
"""
def split_clients(X, y, num_clients=3):
    client_data = []
    split_size = len(X) // num_clients
    for i in range(num_clients):
        start, end = i * split_size, (i + 1) * split_size
        client_data.append((X[start:end], y[start:end]))
    return client_data

def summarize_clients(client_data):
    for i, (X, y) in enumerate(client_data):
        print(f"Client {i+1}: {len(X)} records")
