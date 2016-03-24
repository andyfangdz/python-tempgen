import jinja2
import os

TEMPLATE_DIR = os.path.dirname(__file__)
loader = jinja2.FileSystemLoader([TEMPLATE_DIR], followlinks=True)
env = jinja2.Environment(loader=loader)

templates = {
    'python': {
        'Main': env.get_template('python/Main.py'),
        'Solution': env.get_template('python/Solution.py')
    },
    'java': {
        'Main': env.get_template('java/Main.java'),
        'Solution': env.get_template('java/Solution.java')
    }
}

"""
    'cpp': {
        'compile': env.get_template('cpp/compile.sh'),
        'run': env.get_template('cpp/run.sh'),
        'image': 'gcc'
    },
    'java': {
        'compile': env.get_template('java/compile.sh'),
        'run': env.get_template('java/run.sh'),
        'image': 'vixns/java8'
    },
"""