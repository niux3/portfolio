import os
import importlib
import inspect
from pathlib import Path
import humps
from backend.core.config import config


class Autoload:
    @staticmethod
    def import_models():
        Autoload._import_models_from_package()
        Autoload._import_models_from_file()

    @staticmethod
    def _import_models_from_package():
        registry = dict()
        for file in config.BASEDIR.glob('*/**/models'):
            index_app = str(file).find(str(config.BASEDIR.name))
            namespace = str(file)[index_app:].replace('/', '.')
            if Path(str(file / '__init__.py')).is_file():
                modules_raw = [
                    f.name.rsplit('.').pop(0) 
                    for f in file.glob('*.py') 
                    if not f.name.startswith('__')
                ]
                registry = {
                        humps.pascalize(value): getattr(importlib.import_module(f'{namespace}.{value}'), humps.pascalize(value))
                        for value in modules_raw
                }
                print('>> models (package): ', ', '.join([humps.pascalize(v) for v in modules_raw]), 'loaded!')
        return registry

    @staticmethod
    def _import_models_from_file():
        registry = dict()
        for file in config.BASEDIR.glob('*/**/models.py'):
            index_app = str(file).find(str(config.BASEDIR.name))
            namespace = str(file)[index_app:].replace('/', '.').replace('.py', '')
            module = importlib.import_module(namespace)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, '__tablename__'):
                    registry[name] = getattr(module, name)
            print('>> models (file): ', ', '.join(registry.keys()), 'loaded!')
        return registry

    @staticmethod
    def import_views(app):
        views_loaded = []
        for file in config.BASEDIR.glob('*/**/views'):
            index_app = str(file).find(str(config.BASEDIR.name))
            namespace = str(file)[index_app:].replace('/', '.')
            module = importlib.import_module(namespace)
            for name, obj in inspect.getmembers(module):
                if obj.__class__.__name__ == 'Blueprint':
                    app.register_blueprint(obj)
                    views_loaded.append(name)
        for file in config.BASEDIR.glob('*/**/views.py'):
            index_app = str(file).find(str(config.BASEDIR.name))
            namespace = str(file)[index_app:].replace('/', '.').replace('.py', '')
            module = importlib.import_module(namespace)
            for name, obj in inspect.getmembers(module):
                if obj.__class__.__name__ == 'Blueprint':
                    app.register_blueprint(obj)
                    views_loaded.append(name)
        print('>> views: ', ', '.join(views_loaded), 'loaded!')

    @staticmethod
    def import_errors(app):
        views_loaded = []
        module = importlib.import_module('app.core.errors')
        for name, obj in inspect.getmembers(module):
            if name == 'error_handler':
                for error_status, views in obj.items():
                    app.register_error_handler(error_status, views)
                    views_loaded.append(str(error_status))
        print('>> errors handler:', ', '.join(views_loaded), 'loaded!')
