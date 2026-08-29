'''
Task: Fetch the list of open pull requests from the Kubernetes GitHub page.
The program should print the name of each user and the number of
pull requests opened by that user.
'''

# Import the requests module
import requests

# GitHub API URL
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Fetch information about open pull requests
response = requests.get(url)

# Check whether the request was successful
if response.status_code == 200:

    # Convert the JSON response into Python objects
    pr_details = response.json()

    # Empty dictionary to store users and their PR counts
    pr_creators = {}

    # Iterate through all pull requests
    for pr in pr_details:

        # Get the username of the PR creator
        pr_user = pr["user"]["login"]

        # Increase the PR count if the user already exists
        if pr_user in pr_creators:
            pr_creators[pr_user] += 1

        # Otherwise, add the user with an initial count of 1
        else:
            pr_creators[pr_user] = 1

    # Print the final user details and PR counts
    print("Printing the PR details")

    for pr_user, count in pr_creators.items():
        print(f"{pr_user}: {count} PR(s)")

else:
    print(f"Details not found. Status code: {response.status_code}")