INDEX_URL_PATH: str = "/"

#================================================================================
#                User Story
#================================================================================

#   |
#   V

# User accesses landing page
def test_index_succes(client) -> None:
    #Page loads
    response = client.get(INDEX_URL_PATH)
    assert response.status_code == 200

# or tries to access /index
def test_index_redirect_succes(client) -> None:
    #Page loads
    response = client.get("/index")
    assert response.status_code == 302

#   |
#   V

# Landing page content is rendered
# => test_content.py
def test_index_content(client) -> None:
    # Returns welcome text
    response = client.get(INDEX_URL_PATH)
    assert b"are not embarrassed" in response.data

#   |
#   V

# User accesses contacts
def test_contacts_succes(client) -> None:
    #Page loads
    response = client.get("contact")
    assert response.status_code == 200

# User accesses projects
def test_contacts_succes(client) -> None:
    #Page loads
    response = client.get("projects")
    assert response.status_code == 200