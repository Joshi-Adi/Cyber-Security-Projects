# Simple Phishing Email Detector

# List of suspicious words often used in phishing emails
suspicious_words = ["urgent", "verify", "password", "bank", "login", "click here"]

def check_email(email):
    found = []
    for word in suspicious_words:
        if word.lower() in email.lower():
            found.append(word)
    return found


# Example emails to test
emails = [
    "Your bank account is locked! Please click here to verify your password.",
    "Hello friend, just checking in to confirm our meeting tomorrow."
]

for i, email in enumerate(emails, start=1):
    print(f"\n📩 Email {i}: {email}")
    issues = check_email(email)
    if issues:
        print("⚠️ Possible phishing signs found:", ", ".join(issues))
    else:
        print("✅ No phishing signs detected.")
