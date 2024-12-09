import typer
import os
from InquirerPy import inquirer


app = typer.Typer()

# APP_NAME
# APP_VERSION
# APP_DESCRIPTION
# APP_SLUG
@app.command()
def new(project_name: str | None = None):
    if project_name is None:
        project_name = inquirer.text(message="Enter project name:").execute()
    project_description = inquirer.text(message="Enter project description:").execute()
    project_slug = inquirer.text(message="Enter project slug:").execute()
    project_version = inquirer.text(message="Enter project version:", default='0.1.0').execute()

    os.makedirs(f'tmp/{project_slug}/services', exist_ok=True)
    os.makedirs(f'tmp/{project_slug}/schemas', exist_ok=True)
    os.makedirs(f'tmp/{project_slug}/models', exist_ok=True)
    os.makedirs(f'tmp/{project_slug}/config', exist_ok=True)
    os.makedirs(f'tmp/{project_slug}/routers', exist_ok=True)


@app.command()
def remove(name: str):
    slug = name.lower().replace(' ', '_')
    os.rmdir(f'tmp/{slug}')
