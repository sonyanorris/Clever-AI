import typer
import requests

app = typer.Typer()
API_URL = "http://localhost:8000/land"

@app.command()
def get_land(id: int):
    """Fetch land details by ID."""
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        typer.echo(response.json())
    else:
        typer.echo("Land data not found.")

@app.command()
def add_land(id: int, location: str, price: float):
    """Add a new land record."""
    payload = {"id": id, "location": location, "price": price}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        typer.echo("Land record added successfully!")
    else:
        typer.echo("Failed to add land record.")

if __name__ == "__main__":
    app()
