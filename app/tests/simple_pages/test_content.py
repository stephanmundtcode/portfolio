INDEX_URL_PATH: str = "/"

#================================================================================
#                Content
#================================================================================

# Landing page content is rendered
def test_index_content(client) -> None:
    # Returns welcome text
    response = client.get(INDEX_URL_PATH)
    assert b"are not embarrassed" in response.data