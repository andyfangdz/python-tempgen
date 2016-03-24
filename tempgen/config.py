from templates import templates


def extend(a, b):
    """http://stackoverflow.com/a/12697215/4944625
    Create a new dictionary with a's properties extended by b,
    without overwriting.

    >>> extend({'a':1,'b':2},{'b':3,'c':4})
    {'a': 1, 'c': 4, 'b': 2}
    """
    return dict(b, **a)

config = {
    "languages": {
        "python": {
            "lang": "python",
            "ext": "py",
            "rules": {
                "default": {
                    "encoder": "str"
                },
                "int": {
                    "decoder": "int"
                }
            },
            "templates": {
                "Solution": templates["python"]["Solution"],
                "Main": templates["python"]["Main"]
            }
        },
        "java": {
            "lang": "java",
            "ext": "java",
            "rules": {
                "default": {
                    "encoder": "String.valueOf"
                },
                "int": {
                    "repr": "int",
                    "decoder": "Integer.parseInt"
                }
            },
            "templates": {
                "Solution": templates["java"]["Solution"],
                "Main": templates["java"]["Main"]
            }
        }
    },

    "types": [
        "int"
    ]
}


# Update all rules with defaults w.r.t. their language
for lang in config["languages"]:
    for rule in config["languages"][lang]["rules"]:
        config["languages"][lang]["rules"][rule] = \
            extend(config["languages"][lang]["rules"][rule],
                   config["languages"][lang]["rules"]["default"])

'''
"cpp": {
            "lang": "cpp",
            "ext": "cpp",
            "rules": {
                "default": {
                    "encoder": "to_string"
                },
                "int": {
                    "repr": "int",
                    "parser": "stoi"
                }
            }
        },
'''