import json
import os
import errno


def extend(a, b):
    """http://stackoverflow.com/a/12697215/4944625
    Create a new dictionary with a's properties extended by b,
    without overwriting.

    >>> extend({'a':1,'b':2},{'b':3,'c':4})
    {'a': 1, 'c': 4, 'b': 2}
    """
    return dict(b, **a)


def json_prettyprint(obj):
    return json.dumps(obj,
                      indent=2,
                      separators=(',', ': '))


def mkdir_p(path):
    """http://stackoverflow.com/a/600612/4944625"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def dict_filewritter(path, obj):
    """This one is actually not from Stack Overflow..."""
    mkdir_p(path)
    cur_path = os.path.abspath(path)
    for item in obj:
        if type(obj[item]) is dict:
            target_path = os.path.join(cur_path, item)
            dict_filewritter(target_path, obj[item])
        else:
            with open(os.path.join(cur_path, item), 'w') as file_to_write:
                file_to_write.write(obj[item])
