from jinja2 import (FileSystemLoader,
                    Environment)
from typing import Dict
from pathlib import Path


def load_template(template: str):
    f_loader = FileSystemLoader(Path(__file__).parent / 'templates')
    env = Environment(loader=f_loader)
    template_obj = env.get_template(template)
    return template_obj


def render_template(class_: str, item: Dict) -> str:
    template_obj = load_template(template=f'wiki_{class_}.jinja')
    wiki_item = template_obj.render(wikitemplate=class_,
                                    item_dict=item)
    print(wiki_item)
    return wiki_item
