import os

# Configuration settings
RECIPIENTS = ['deonb23@gmail.com']

# Email Settings
# Ideally, these should be loaded from environment variables for security.
# For this task, we will check for environment variables, and if not present,
# we will prompt or default to a safe "Mock" mode in the main script.
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'deonb23@gmail.com'
SENDER_PASSWORD = 'Flugelbind23#' # Google Account App Password
