import requests
import json
import sys
from enum import Enum

from api.enum.endpoint_crud import EndpointCrud
from dal.utils.enums import Table, UserCol
from il import EnvironmentVariable as Env

def get(val: Enum) -> str:
    return val.value

ENTITY_TABLE = Table.USER.value
ENTITY = UserCol

CREATE_PAYLOAD ={
        f"{get(ENTITY.USERNAME)}": "Nouveau",
        f"{get(ENTITY.EMAIL)}": "mich@example.com"
    }
UPDATE_PAYLOAD ={
        f"{get(ENTITY.USERNAME)}": "Nouveau2",
        f"{get(ENTITY.EMAIL)}": "mich2@example.com"
    }
GET_COL = get(ENTITY.USERNAME)

CRUD = EndpointCrud
BASE = f"http://{Env.HOST.get()}:{Env.PORT.get()}/{ENTITY_TABLE}"
HEADERS = {"Content-Type": "application/json"}

#region LOGIC
def pretty(resp):
    try:
        data = resp.json()
    except ValueError:
        print("<no JSON>")
        return
    print(f"Status: {resp.status_code}")
    print(json.dumps(data, indent=2, ensure_ascii=False))
def test():
    print(f"\nGET {BASE}") # GET all
    pretty(requests.get(f"{BASE}"))

    print(f"\nPOST {BASE}") # POST create
    pretty(requests.post(f"{BASE}", headers=HEADERS, json=CREATE_PAYLOAD))

    print("\nGET /posts/1") # GET by id
    pretty(requests.get(f"{BASE}/1"))

    print("\nGET /posts/by/title/Nouveau") # GET by title
    pretty(requests.get(f"{BASE}{get(CRUD.GET_BY)}/{GET_COL}/Nouveau"))

    print("\nPUT /posts/1")   # PUT update
    pretty(requests.put(f"{BASE}/1", headers=HEADERS, json=UPDATE_PAYLOAD))

    print("\nDELETE /posts/1") # DELETE
    resp = requests.delete(f"{BASE}/1")
    print(f"Status: {resp.status_code}")
#endregion

if __name__ == '__main__':
    test()