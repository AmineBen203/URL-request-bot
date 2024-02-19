import requests
import time

# Set the timeout duration in seconds for each request
request_timeout = 5  # Adjust as needed

# Number of requests to make
num_requests = 30

# URL to visit
url = "https://github.com/AmineBen203"

# Loop for making requests
for i in range(num_requests):
    try:
        # Record the start time for each request
        start_time = time.time()

        # Make a request to the website
        response = requests.get(url, timeout=request_timeout)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request", i+1, "successful")
        else:
            print("Request", i+1, "failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request", i+1, "failed:", e)

    # Calculate elapsed time for the request
    elapsed_time = time.time() - start_time

    # Add a small delay to avoid overwhelming the server
    time.sleep(1)  # Adjust as needed

print("All requests completed.")
