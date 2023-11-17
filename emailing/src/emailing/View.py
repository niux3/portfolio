from jinja2 import Template

class View:
    @staticmethod
    def get(path):
        with open(path, 'r') as resource:
            tpl = Template(resource.read())
        return tpl
