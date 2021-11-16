from flask.cli import AppGroup
from .users import (seed_users, undo_users, seed_entries, undo_entries,
    seed_journals, undo_journals, seed_tags, undo_tags,
    seed_entries_tag, undo_entries_tag)

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_entries()
    seed_journals()
    seed_tags()
    seed_entries_tag()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_entries()
    undo_journals()
    undo_tags()
    undo_entries_tag()
    # Add other undo functions here
