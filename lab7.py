import sys

def is_palindrome(text):
    # Clean string: lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Uses command-line argument if provided, otherwise defaults to "madam"
    sample_text = sys.argv[1] if len(sys.argv) > 1 else "madam"
    
    if is_palindrome(sample_text):
        print(f"'{sample_text}' is a palindrome.")
    else:
        print(f"'{sample_text}' is NOT a palindrome.")
