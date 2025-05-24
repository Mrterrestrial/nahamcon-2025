import re

def extract_valid_flags(file_path):
    """
    Extracts valid flags that match the format: flag{32 lowercase hex chars}
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Regex for valid lowercase hex-only 32-character flags
    pattern = r"flag\{[0-9a-f]{32}\}"
    valid_flags = re.findall(pattern, content)
    
    if valid_flags:
        print("Valid Hex Flags:")
        for flag in valid_flags:
            print(flag)
    else:
        print("No valid flags found.")


extract_valid_flags("free_flags.txt")
