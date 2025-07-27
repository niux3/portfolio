from backend.core.config import config
from flask import request


def inject_footer_flag():
    def context():
        endpoints_without_footer = {
            "posts.show",
        }
        return {
            "display_buttons_footer": request.endpoint not in endpoints_without_footer
        }
    return context

def inject_base_url_project():
    def context():
        return {'base_url_project': config.URL_PROJECT}
    return context

def inject_og_image():
    def context():
        full_url = f'{config.URL_PROJECT}/static/img/og_image_rb_webstudio.svg'
        return dict(full_url_og_img=full_url)
    return context
