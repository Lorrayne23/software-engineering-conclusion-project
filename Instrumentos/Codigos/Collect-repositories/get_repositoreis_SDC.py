import pandas as pd
import requests
import time
from datetime import datetime
from datetime import date

token = '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'

headers = {"Authorization": f"Bearer {token}"}

def run_query(cursor):
    f_cursor = "null" if cursor is None else "\"" + cursor + "\""
    query = """{
  search(
    query:"topic:self-driving-car language:python"
    type: REPOSITORY
    first: 100
    after: """ + f_cursor + """
  ) {
    pageInfo {
      endCursor
      hasNextPage
    }
    nodes {
      ... on Repository {
        name
        nameWithOwner
        url
        updatedAt
        releases {
          totalCount
        }
      }
    }
  }
}
"""
    downloaded = False
    while not downloaded:
        try:
            request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
            if request.status_code == 200:
                return request.json()
            else:
                raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        except:
            time.sleep(2)
            continue

data = []
def save_file(result):
  results = result["data"]["search"]["nodes"]
  for r in results:
    name = r["name"]
    name_with_owner = r["nameWithOwner"]
    url_repository = r["url"]
    updatedAt = r["updatedAt"]
    num_of_releases = r['releases']['totalCount']
    data.append([name, name_with_owner, url_repository,updatedAt, num_of_releases])
    columns = ["Name", "NameWithOwner","Url", "UpdateAt", "Num_of_Releases"]
    df = pd.DataFrame(data, columns=columns)
    df = df.set_index('Name')
    df.to_csv("./Collect-repositories/repositories-self-driving-cars.csv")

pages = 10
endCursor = None
for page in range(pages):
    result = run_query(endCursor)
    save_file(result)
    has_next = result["data"]["search"]["pageInfo"]["hasNextPage"]
    if not has_next:
        break
    endCursor = result["data"]["search"]["pageInfo"]["endCursor"]