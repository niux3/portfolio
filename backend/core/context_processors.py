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
