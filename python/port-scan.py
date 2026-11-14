import socket  # Built-in module for network connections

# 1. Define which TCP ports you want to test on every server
ports_to_check = [22, 80, 443, 4096]

# Set a timeout in seconds so the script doesn't hang forever on blocked ports
CONNECTION_TIMEOUT = 2.0 

print("🔒 Starting automated TCP Port Scan...")
print("-" * 55)

# 2. Open and read your server text file
with open("servers1.txt", "r") as file:
    for line in file:
        server = line.strip()
        
        # Skip empty lines
        if not server:
            continue
            
        print(f"Checking ports on: {server}")
        
        # 3. Loop through each port for the current server
        for port in ports_to_check:
            
            # Create a network socket connection box (AF_INET = IPv4, SOCK_STREAM = TCP)
            # 'with' ensures the socket safely closes right after checking
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(CONNECTION_TIMEOUT)
                
                # connect_ex returns an error code instead of throwing a full script crash
                result = s.connect_ex((server, port))
                
                # An error code of 0 means the connection succeeded!
                if result == 0:
                    print(f"  -> Port {port}: 🟢 OPEN")
                else:
                    print(f"  -> Port {port}: 🔴 CLOSED / FILTERED")
        print() # Print an empty line between servers for clean layout

print("-" * 55)
print("Port scan complete!")

