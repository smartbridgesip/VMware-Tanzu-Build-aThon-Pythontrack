import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
Hello="message"
sg = sendgrid.SendGridAPIClient('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')
from_email = Email("sandeep@thesmartbridge.com")  # Change to your verified sender
to_email = To("pradeepthi@thesmartbridge.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain",Hello)
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)