from config import config


def patch_param(param, lang):
    lang_rules = config["languages"][lang]["rules"]
    param.update(lang_rules[param["type"]])
    return param


def patch(problem, lang):
    problem["params"] = [
        patch_param(param, lang)
        for param in problem["params"]
    ]
    return problem


def transform(problem, language=None):
    result = {}

    if language is None:
        for lang in config["languages"].keys():
            result[lang] = transform(problem, language=lang)
        return result

    lang_conf = config["languages"][language]
    templates = config["languages"][language]["templates"]

    problem_copy = problem.copy()
    patch(problem_copy, lang=language)
    patch_param(problem_copy["return"], lang=language)

    for template in templates:
        result["{}.{}".format(template, lang_conf["ext"])] = templates[template].render(problem_copy)

    return result
