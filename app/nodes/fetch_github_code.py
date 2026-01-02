import os
from app.github.github_client import fetch_repo_tree, fetch_file_content

def fetch_github_code():
    owner = os.getenv("GITHUB_OWNER")
    repo = os.getenv("GITHUB_REPO")
    branch = os.getenv("GITHUB_BRANCH", "main")

    tree = fetch_repo_tree(owner, repo, branch)

    java_files = [item["path"] for item in tree if item["path"].endswith(".java")]

    code_chunks = []

    for path in java_files:
        code : fetch_file_content(owner, repo, path, branch)
        code_chunks.append(code)

    return {
        "files": java_files,
        "code_chunks": code_chunks
    }