from http import client
from fastapi.testclient import TestClient
from urllib import response
from pydoc import cli

from main import app

client=TestClient(app)

def test_create_event():
    response=client.post("/"
    ,
    json={ "name":"name of todo",
            "description":"this is todo",
            "priority":1,
            "eventdate":"05-10-2021"
    }
            )
    assert response.status_code==200
    test_out=response.json()[0]
    global test_id
    test_id=test_out['id']
    assert test_out["name"]=="name of todo"
    print(test_id)

def test_find_one_event():
        # print(test_id)
        res="/"+test_id
        response=client.get(res)
        assert response.status_code==200
        test_out=response.json()
        assert test_out["name"]=="name of todo"

def test_update_event():
        res="/"+test_id
        response=client.put(res,json={ "name":"changed name",
            "description":"this is todo",
            "priority":1,
            "eventdate":"05-10-2021"
    }
    )
        assert response.status_code==200
        test_out=response.json()
        assert test_out["name"]=="changed name"

def test_delete_event():
        res='/'+test_id
        response=client.delete(res)
        assert response.status_code==200