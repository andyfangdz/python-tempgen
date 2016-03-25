from __future__ import print_function
from tempgen import transform
import json
import click
from config import config
from utils import json_prettyprint, dict_filewritter

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


@click.command()
@click.option('--example', '-e', is_flag=True, help='Show A + B example')
@click.argument('write_to', default='', required=False, type=click.Path(exists=True))
def main(write_to, example):
    """Generates LintCode template."""
    print(write_to)
    if example:
        problem = example_aplusb
    else:
        unsatisfied = True
        while unsatisfied:
            problem = {}
            available_types = '(%s)' % ', '.join(config["types"])

            problem["classname"] = click.prompt('Class Name', show_default=True, default="Solution")
            problem["methodname"] = click.prompt('Method Name', show_default=True, default="aplusb")
            problem["hint"] = click.prompt('Hint', show_default=True,
                                           default="write your code here, try to do it without arithmetic operators.")

            problem["return"] = {}
            problem["return"]["type"] = click.prompt('Return Type ' + available_types, show_default=True, default="int")
            problem["return"]["desc"] = click.prompt('Return Description', show_default=True,
                                                            default="The sum of a and b")

            more_params = True
            problem["params"] = []
            while more_params:
                param_id = len(problem["params"]) + 1
                param = {}
                click.echo("Param %d" % param_id)
                param["name"] = click.prompt('Param Name', show_default=True, default="a")
                param["type"] = click.prompt('Param Type ' + available_types, show_default=True, default="int")
                param["desc"] = click.prompt('Param Description', show_default=True,
                                                    default="An integer")
                more_params = False
                if click.confirm('Add more params?', show_default=True):
                    more_params = True
                problem["params"].append(param)

            click.echo(json_prettyprint(problem))
            if click.confirm('Does this look good?', show_default=True):
                unsatisfied = False

    if write_to:
        dict_filewritter(write_to, transform(problem))
    else:
        click.echo(json_prettyprint(transform(problem)))
