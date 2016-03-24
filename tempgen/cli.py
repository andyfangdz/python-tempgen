from __future__ import print_function
from tempgen import transform
import json
import click

example_aplusb = {
    "classname": "Solution",
    "methodname": "aplusb",
    "params": [
        {"name": "a", "desc": "The first integer", "type": "int"},
        {"name": "b", "desc": "The second integer", "type": "int"}
    ],
    "return": {
        "type": "int",
        "desc": "The sum of a and b"
    },
    "hint": "write your code here, try to do it without arithmetic operators."
}


def json_prettyprint(obj):
    return json.dumps(obj,
                     indent=2,
                     separators=(',', ': '))


@click.command()
@click.option('--example', '-e', is_flag=True, help='Show A + B example')
@click.argument('language', default='', required=False)
def main(language, example):
    """Generates LintCode template."""
    if example:
        problem = example_aplusb
    click.echo(json_prettyprint(transform(problem)))
