from app.projects.routes import load_json

PROJECT_DATA_PATH: str = "app/mock_data/projects.json"

#================================================================================
#                User Story
#================================================================================

#   |
#   V

# User accesses projects page
def test_projects_success(client):
    #Loading page
    response = client.get("/projects")
    assert response.status_code == 200

#   |
#   V

# User accesses individual project pages
def test_all_individual_projects_success(client):
    #Loading page
    projects = load_json(PROJECT_DATA_PATH)
    for project in projects:

        response = client.get(f"/projects/{project["slug"]}")
        assert response.status_code == 200

def test_invalid_project_slug(client):
    response = client.get(f"/projects/blablabla")
    assert response.status_code == 404