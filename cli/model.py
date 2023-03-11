"""model module for the cli app"""
import click
# import the migrate functions from respective modules
client:str = ""
random_data = dict()
migrate_tasks = dict()


@click.group()
def cli():
    """Welcome to the RestaurantOne Management System CLI.
    """


@click.command()
def migrate():
    """migrate models to the database"""
    click.echo('Migrating data into the database')
    # call the migrate function from the respective module
    click.echo('Migration completed successfully')


@click.command()
def populate_db():
    """load data to the database"""
    click.echo('Loading data into the database')
    # call the load_data function from the respective module
    click.echo('Data loaded successfully')


cli.add_command(migrate)
cli.add_command(populate_db)
