from __future__ import print_function
from tempgen import transform
import json
import click
from config import config

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
            problem["return"]["description"] = click.prompt('Return Description', show_default=True,
                                                            default="The sum of a and b")

            more_params = True
            problem["params"] = []
            while more_params:
                param_id = len(problem["params"]) + 1
                param = {}
                click.echo("Param %d" % param_id)
                param["type"] = click.prompt('Param Type ' + available_types, show_default=True, default="int")
                param["description"] = click.prompt('Param Description', show_default=True,
                                                            default="An integer")
                more_params = False
                if click.confirm('Add more params?', show_default=True):
                    more_params = True
                problem["params"].append(param)

            click.echo(json_prettyprint(problem))
            if click.confirm('Does this look good?', show_default=True):
                unsatisfied = False

    click.echo(json_prettyprint(transform(problem)))
