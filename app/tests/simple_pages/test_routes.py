
#================================================================================
#                User Story
#================================================================================

#   |
#   V

# User accesses landing page
def test_index_succes(client):
    #Page loads
    response = client.get("/")
    assert response.status_code == 200

# or tries to access /index
def test_index_redirect_succes(client):
    #Page loads
    response = client.get("/index")
    assert response.status_code == 302

#   |
#   V

# User accesses contacts
def test_contacts_succes(client):
    #Page loads
    response = client.get("contact")
    assert response.status_code == 200