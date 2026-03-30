from app.projects.routes import load_json

PROJECT_DATA_PATH: str = "app/mock_data/projects.json"
PROJECTS_URL_PATH: str = "/projects"

PROJECTS = load_json(PROJECT_DATA_PATH)

#================================================================================
#                User Story
#================================================================================

#   |
#   V

# User accesses projects page
def test_projects_success(client) -> None:
    #Loading page
    response = client.get(PROJECTS_URL_PATH)
    assert response.status_code == 200

#   |
#   V

# User accesses individual project pages
def test_all_individual_projects_success(client) -> None:

    #Loading page
    for project in PROJECTS:
        response = client.get(f"{PROJECTS_URL_PATH}/{project["slug"]}")
        assert response.status_code == 200

def test_invalid_project_slug(client) -> None:
    response = client.get(f"{PROJECTS_URL_PATH}/blablabla")
    assert response.status_code == 404