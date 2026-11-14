##-Server-report-check.2
import subprocess  # Module to execute system terminal commands
import platform    # Module to detect if you are running on Windows, Linux, or Mac

# 1. Your list of targets to check (Can be server IPs or web domain names)
servers_to_test = ["google.com", "8.8.8.8", "192.168.1.254", "invalid.server.test", "10.10.11.221"]

print("⚡ Starting Real-Time Network Ping Scan...")
print("-" * 55)

# 2. Configure the ping options based on your Operating System
# Windows uses '-n' to limit pings, Linux/Mac uses '-c'
current_os = platform.system().lower()
ping_flag = "-n" if current_os == "windows" else "-c"

healthy_count = 0
failed_count = 0

# 3. The Loop
for server in servers_to_test:
    print(f"Pinging {server}...")
    
    # Run the real terminal ping command behind the scenes
    # We ping exactly 1 time, and hide the messy text output using stdout/stderr flags
    result = subprocess.run(
        ["ping", ping_flag, "1", server],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # 4. Evaluate the Exit Code
    # An exit code of 0 means the command succeeded (Server responded!)
    if result.returncode == 0:
        print(f"-> 🟢 {server} is REACHABLE\n")
        healthy_count = healthy_count + 1
    else:
        print(f"-> 🔴 {server} is UNREACHABLE / DOWN\n")
        failed_count = failed_count + 1

# 5. Summary Report
print("-" * 55)
print("📊 SCAN SUMMARY REPORT")
print("-" * 55)
print(f"Total Targets Checked : {len(servers_to_test)}")
print(f"Online / Responsive   : {healthy_count}")
print(f"Offline / Unreachable : {failed_count}")
print("-" * 55)

