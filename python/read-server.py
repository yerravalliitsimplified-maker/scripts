##-read_servers.py
print("--- Reading Server List File ---")
# 1. Open the file in 'r' (read ) mode
with open ("servers.txt", "r") as file:

    # 2. Loop through every line inside the file box
    for line in file:

        # 3. Clean up the invisible newline gaps (\n) at the end of the line
        cleaned_line = line.strip()

        # 4. Only print the line if it isn't completely empty
        if cleaned_line:
            print(f"Server Data found: {cleaned_line}")

print("**************************")
            
