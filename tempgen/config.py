from templates import templates
from utils import extend


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
        },
        "cpp": {
            "lang": "cpp",
            "ext": "cpp",
            "rules": {
                "default": {
                    "encoder": "to_string"
                },
                "int": {
                    "repr": "int",
                    "decoder": "stoi"
                },
            },
            "templates": {
                "Solution": templates["cpp"]["Solution"],
                "Main": templates["cpp"]["Main"]
            }
        },
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
