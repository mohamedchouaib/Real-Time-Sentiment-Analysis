import json
import socket
import time
import pandas as pd

def handle_date(obj):
    if isinstance(obj, pd.Timestamp):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def send_data_over_socket(file_path, host='spark-master', port=9999, chunk_size=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Listening for connections on {host}:{port}")

    last_sent_index = 0
    try:
        # Load the entire JSON data at once
        with open(file_path, 'r') as file:
            data = json.load(file)  # Assuming the data is a JSON array

        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            try:
                # Send data in chunks
                for i in range(last_sent_index, len(data), chunk_size):
                    chunk = pd.DataFrame(data[i:i+chunk_size])
                    # Convert 'DateTime' strings to pd.Timestamp
                    chunk['DateTime'] = pd.to_datetime(chunk['DateTime'])
                    print(chunk)
                    for record in chunk.to_dict(orient='records'):
                        serialize_data = json.dumps(record, default=handle_date).encode('utf-8')
                        conn.send(serialize_data + b'\n')
                        time.sleep(5)
                    
                    last_sent_index += chunk_size

            except (BrokenPipeError, ConnectionResetError):
                print("Client disconnected.")
            finally:
                conn.close()
                print("Connection closed")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_data_over_socket("datasets/Weather_Data.json")
