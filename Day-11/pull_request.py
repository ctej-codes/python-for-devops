# To fetch the pull request from Git hub K8s repo

import requests # to do the api calls use this module

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
pr_details = response.json()

for pr in pr_details:
    print(pr["user"]["login"])