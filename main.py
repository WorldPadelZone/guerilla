import config
from email_service import EmailService

def load_template(filename):
    """Loads the HTML template from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None

def main():
    print("--- Guerilla AI Training Automation ---")
    
    # Load content
    template_file = 'foundations.html'
    content = load_template(template_file)
    
    if not content:
        return

    # Initialize Service
    service = EmailService()

    # Send to recipients
    subject = "Guerilla AI Training: Module 1 - Foundations"
    
    for recipient in config.RECIPIENTS:
        print(f"Processing recipient: {recipient}")
        service.send_email(recipient, subject, content)

    print("--- Batch Complete ---")

if __name__ == "__main__":
    main()
