#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)


def configure_log(app):
    if not app.debug:
        import logging
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

if __name__ == '__main__':
    # configure_log(app)
    socketio.run(app)
