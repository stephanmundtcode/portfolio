from app.projects.routes import load_json

PROJECT_DATA_PATH: str = "app/mock_data/projects.json"
PROJECTS_URL_PATH: str = "/projects"

PROJECTS = load_json(PROJECT_DATA_PATH)

# project page content is rendered
def test_projects_content(client) -> None:
    # Returns welcome text
    response = client.get(PROJECTS_URL_PATH)
    assert b"My Projects" in response.data
    for project in PROJECTS:
        assert f"{project["title"]}" in response.text