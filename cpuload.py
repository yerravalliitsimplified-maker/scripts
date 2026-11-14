cpu_usage = 85

if cpu_usage >= 90:
    print("🚨 CRITICAL: CPU is dangerously high!")
elif cpu_usage >= 70:
    print("⚠️ WARNING: CPU usage is getting high.")
else:
    print("✅ OK: CPU usage is normal.")

