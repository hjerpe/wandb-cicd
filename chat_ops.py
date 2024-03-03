import os
from ghapi.all import GhApi
owner, repo = os.environ['GITHUB_REPOSITORY'].split('/')
api = GhApi(owner=owner, repo=repo, token=os.environ['GITHUB_TOKEN'])
PR_NUMBER = os.environ['PR_NUMBER']
comments = api.pulls.get_review_comment(owner=owner, repo=repo, comment_id=PR_NUMBER)
print(comments)