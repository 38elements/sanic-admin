import sys
from importlib import machinery, util


def run(setting):
    paths = sys.argv[:]
    paths.remove('-urls')
    path = paths[-1]
    loader = machinery.SourceFileLoader('server', path)
    spec = util.spec_from_loader(loader.name, loader)
    module = util.module_from_spec(spec)
    loader.exec_module(module)
    app = getattr(module, setting['app'])
    for key, route in app.router.routes_all.items():
        print(key + '  ' + ','.join(route.methods))


if __name__ == '__main__':
    import os
    run({
        'paths': [os.getcwd()],
        'patterns': ['*.py'],
        'before': None,
        'before_each': None,
        'after': None,
        'after_each': None,
        'app': 'app'
    })
