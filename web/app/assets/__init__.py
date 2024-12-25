import os
import json

from flask import Flask


def asset_url(asset_name):
    from flask import current_app, url_for

    # return the URL to the Vite dev server in debug mode
    # and the URL to the hashed asset in production mode

    if current_app.debug:
        server_url = "http://localhost:5173"

        return f"{server_url}/{asset_name}"

    manifest_path = os.path.join(current_app.static_folder, "assets/manifest.json")

    try:
        with open(manifest_path, "r") as manifest_file:
            manifest = json.load(manifest_file)

        hashed_file = manifest[asset_name]["file"]

        return url_for("static", filename=hashed_file)

    except FileNotFoundError:
        raise RuntimeError(f"Manifest file was not found at {manifest_path}")

    except KeyError:
        raise RuntimeError(f"{asset_name} is not in the manifest")


def initialize(app: Flask):
    @app.context_processor
    def inject_asset_url():
        return { "asset_url": asset_url }
