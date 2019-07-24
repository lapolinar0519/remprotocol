"""
Provide implementation of the command line interface to interact with token swap contracts.
"""
import click

from cli.eth_swap_bot.cli import eth_swap_bot_commands
from cli.remchain_swap_contract.cli import remchain_swap_contract_commands


@click.group()
@click.version_option()
@click.help_option()
def cli():
    """
    Command-line interface to interact with token swap contracts.
    """
    pass


cli.add_command(eth_swap_bot_commands)
cli.add_command(remchain_swap_contract_commands)
