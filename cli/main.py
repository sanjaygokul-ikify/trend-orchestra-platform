import click
from ..services import orchestrator

@click.command()
def main():
    engine = Engine({"agent1": Agent("agent1", "agent1")})
    orchestrator = orchestrator.Orchestrator(engine)
    orchestrator.start()