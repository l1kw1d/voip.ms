import sys
from zeep import Client

# API credentials
API_USERNAME = "johndo@youremail.com"
API_PASSWORD = "your_api_password_from_the_dashboard"

# Create a SOAP client with the server.wsdl file path or URL
client = Client('path/to/server.wsdl')

# Extract the arguments from command-line input
arguments = sys.argv[1:]

for argument in arguments:
    # Prepare the request parameters
    request_data = {
        'api_username': API_USERNAME,
        'api_password': API_PASSWORD,
        'did': 'your_voip.ms_did_number',
        'dst': 'your_destination_number',
        'message': argument
    }

    # Send the SOAP request
    response = client.service.sendSMS(request_data)

    # Process the response
    if response['result'] == 'success':
        print(f"SMS sent successfully! Argument: {argument}")
    else:
        print(f"SMS sending failed. Argument: {argument}. Error message: {response['result']}")
