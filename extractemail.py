import re #re Python's built-in module for finding patterns inside text

def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f: # opens and reads the txt file in read-only + handle special characters
        text = f.read() #reads the entire file content into a single string variable called text

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #username part(khansa) +sign(@) + domain name(gmail) + dot + extension atleat 2(.com)
    emails = sorted(set(re.findall(pattern, text))) #Find all+remove dupicated+sorted

    with open(output_file, "w", encoding="utf-8") as f: # create new ouput file and write the unique emails to it
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique emails, saved to {output_file}")

# Text file containing emails and output file for unique emails
extract_emails("input.txt", "emails.txt")