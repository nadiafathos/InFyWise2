from http import HTTPStatus

import pytest

from api.enum.endpoint_crud import EndpointCrud
from dal.utils.enums import Table, UserCol, PostCol, TagCol


def get_base_url(table_name: Table):
    return f'/{table_name.value}'
ID = 'id'

@pytest.mark.order(1)
def test_user_crud(client):

    rv = assert_create( # CREATE
        client.post(get_base_url(Table.USER), json={f'{UserCol.USERNAME.value}': "michel", f'{UserCol.EMAIL.value}': "michel@example.com"})
    )
    uid = rv.get_json()[ID]

    assert_get(client.get(get_base_url(Table.USER))) # GET ALL
    assert_get(client.get(f"{get_base_url(Table.USER)}/{uid}")) # GET BY ID
    assert_get(client.get(f"{get_base_url(Table.USER)}{EndpointCrud.GET_BY.value}/{UserCol.USERNAME.value}/michel")) # GET BY COLUMN

    assert_update(  # UPDATE
        client.put(
            f'{get_base_url(Table.USER)}/{uid}',
            json={f'{UserCol.USERNAME.value}': "michel le retour", f'{UserCol.EMAIL.value}': "michel@example.com"}),
            UserCol.USERNAME.value,
            "michel le retour"
    )

    # CLEANUP
    assert client.delete(f"{get_base_url(Table.USER)}/{uid}").status_code == HTTPStatus.NO_CONTENT

@pytest.mark.order(2)
def test_tag_crud(client):

    rv = assert_create( # CREATE
        client.post(
            get_base_url(Table.TAG),
            json={ f'{TagCol.NAME.value}': "tag1" }
    ))
    tid = rv.get_json()[ ID ]


    assert_get( # GET ALL
        client.get( get_base_url(Table.TAG) )
    )


    assert_get( # GET BY ID
        client.get( f"{get_base_url(Table.TAG)}/{tid}" )
    )


    assert_get( # GET BY COLUMN
        client.get(
            f"{get_base_url(Table.TAG)}{EndpointCrud.GET_BY.value}/{TagCol.NAME.value}/tag1"
    ))

    # UPDATE
    assert_update(
        client.put(
            f"{get_base_url(Table.TAG)}/{tid}",
            json={ f'{TagCol.NAME.value}': "tag2" }
        ),
        TagCol.NAME.value,
        "tag2"
    )

    # CLEANUP
    assert client.delete(f"{get_base_url(Table.TAG)}/{tid}").status_code == HTTPStatus.NO_CONTENT

@pytest.mark.order(3)
def test_post_crud(client):
    rv = client.post(get_base_url(Table.USER), json={f'{UserCol.USERNAME.value}':"mich", f'{UserCol.EMAIL.value}':"mich@example.com"})
    uid = rv.get_json()[ID]

    rv = client.post(get_base_url(Table.TAG), json={ f'{TagCol.NAME.value}':"t1"})
    tid = rv.get_json()[ID]
    pid = rv.get_json()[ID]

    # CREATE
    assert_create(
        client.post(
            get_base_url(Table.POST),
            json={
                f'{PostCol.TITLE.value}':"Mon titre",
                f'{PostCol.CONTENT.value}':"Un contenu",
                f'{PostCol.FK_AUTHOR.value}': uid,
                f'{PostCol.AUTHOR.value}':[{ f'{TagCol.NAME.value}':"t1" }]
            }
    ))

    assert_get(client.get(f"{get_base_url(Table.POST)}")) # GET ALL
    assert_get(client.get(f"{get_base_url(Table.POST)}/{pid}")) # GET BY ID
    assert_get(client.get(f"{get_base_url(Table.POST)}{EndpointCrud.GET_BY.value}/{PostCol.TITLE.value}/Mon titre")) # GET BY COLUMN

    assert_update( # UPDATE
        client.put(f"{get_base_url(Table.POST)}/{pid}", json={
            f'{PostCol.TITLE.value}': "Nouveau Titre",
            f'{PostCol.CONTENT.value}': "Nouveau contenu",
            f'{PostCol.FK_AUTHOR.value}': uid,
            f'{PostCol.AUTHOR.value}': [{f'{TagCol.NAME.value}': "t1"}]
        }),
        PostCol.TITLE.value,
        "Nouveau Titre"
    )

    # CLEANUP
    assert client.delete(f"{get_base_url(Table.POST)}/{pid}").status_code == HTTPStatus.NO_CONTENT
    assert client.delete(f"{get_base_url(Table.TAG)}/{tid}").status_code == HTTPStatus.NO_CONTENT
    assert client.delete(f"{get_base_url(Table.USER)}/{uid}").status_code == HTTPStatus.NO_CONTENT

def assert_get(rv : any):
    assert rv.status_code == HTTPStatus.OK

def assert_create(rv : any):
    assert rv.status_code == HTTPStatus.CREATED
    return rv

def assert_update(rv : any, col_name: str, value: any):
    assert rv.status_code == HTTPStatus.OK
    assert rv.get_json()[col_name] == value
    return rv