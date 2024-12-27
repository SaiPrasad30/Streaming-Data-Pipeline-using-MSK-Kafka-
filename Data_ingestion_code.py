import requests
import json

# API Gateway Invoke URL
api_url = "<Your Api URL>"

# Message to send to the API
message = {
    "MessageBody": "Hello World!"
}

temp = 0;

while temp < 100:

  try:
      # Send POST request to API Gateway
      response = requests.post(
          api_url,
          headers={
              "Content-Type": "application/json"  # Set the correct content type
          },
          data=json.dumps(message)  # Convert Python dictionary to JSON
      )

      # Check if the request was successful
      if response.status_code == 200:
          print("Message sent successfully!")
          try:
              # Attempt to parse the response as JSON
              response_data = response.json()
              print("Response:", response_data)
          except json.JSONDecodeError:
              print("Response body is empty.")
      else:
          print(f"Failed to send message. Status Code: {response.status_code}")
          print("Error Response:", response.text)

  except Exception as e:
      print("An error occurred:", str(e))

  temp = temp + 1;
