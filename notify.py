import socket, sys, time

host = sys.argv[1]
port = int(sys.argv[2])

for attempt in range(1, 6):
    print(f"=== Notify attempt {attempt}/5 ===")
    try:
        with socket.create_connection((host, port), timeout=10) as s:
            s.sendall(b"build_ok")
            resp = s.recv(2)
            if resp:
                print("Server notified successfully.")
                sys.exit(0)
    except Exception as e:
        print(f"Failed: {e}")
    if attempt < 5:
        time.sleep(5)

print("All attempts failed.")
sys.exit(1)
