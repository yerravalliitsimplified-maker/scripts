##-Server_report.py
import random  # Module to help us simulate random server uptimes
import time    # Module to add a slight delay for realism

# 1. Our Data Container (List of Dictionaries)
servers_to_check = [
    {"name": "server01", "ip": "192.168.1.10"},
    {"name": "server02", "ip": "192.168.1.11"},
    {"name": "server03", "ip": "192.168.1.12"},
    {"name": "server04", "ip": "192.168.1.13"}
]
# 2. Reusable Function to evaluate server health
def evaluate_uptime(uptime_percentage):
    if uptime_percentage >= 99.0:
        return "✅ EXCELLENT"
    elif uptime_percentage >= 95.0:
        return "⚠️ WARNING (Low Uptime)"
    else:
        return "🚨 CRITICAL (Action Required)"

# 3. Variables to keep track of our final report numbers
total_checked = 0
issues_found = 0

print("🔍 Starting Infrastructure Health Scan...")
print("-" * 50)

# 4. The Loop
for server in servers_to_check:
    total_checked = total_checked + 1
    print(f"Checking {server['name']} ({server['ip']})...")
    
    # Simulate data: picks a random decimal number between 90.0 and 100.0
    simulated_uptime = round(random.uniform(90.0, 100.0), 2)
    
    # Pass the number into our function to get a status string
    status = evaluate_uptime(simulated_uptime)
    
    # Look inside the status string to count issues
    if "✅" not in status:
        issues_found = issues_found + 1
        
    print(f"-> Result: {simulated_uptime}% Uptime | {status}\n")
    time.sleep(0.5)  # Pause for half a second before checking the next one

    # 5. Final Report Summary using F-Strings
print("-" * 50)
print("📊 FINAL SCAN REPORT")
print("-" * 50)
print(f"Total Servers Checked : {total_checked}")
print(f"Healthy Servers       : {total_checked - issues_found}")
print(f"Servers with Issues   : {issues_found}")
print("*" * 50)
#print("-" * 50)
