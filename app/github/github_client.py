import requests
import base64
import os


GITHUB_API = "https://api.github.com"

def fetch_repo_tree(owner: str, repo: str, branch: str):
     headers = {"Authorization": f"token {token}"} if token else {}
     url = f"{GITHUB_API}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
     response = requests.get(url, headers=headers)
     response.raise_for_status()

     return response.json().get("tree", [])
def fetch_file_content(owner: str, repo: str, path: str, branch: str):
     headers = {"Authorization": f"token {token}"} if token else {}
     url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
     response = requests.get(url, headers=headers)
     response.raise_for_status()

     content = response.json()["content"]
     return base64.b64decode(content).decode("utf-8")
