import logging
import os

from flask import Flask, request
from google.cloud import storage
import flask
import werkzeug.datastructures


app = flask.Flask(__name__)
def superresolution_upload_image(request):
    with app.app_context():
        headers = werkzeug.datastructures.Headers()
        for key, value in request.headers.items():
            headers.add(key, value)
        with app.test_request_context(method=request.method, base_url=request.base_url, path=request.path, query_string=request.query_string, headers=headers, data=request.data):
            try:
                rv = app.preprocess_request()
                if rv is None:
                    rv = app.dispatch_request()
            except Exception as e:
                rv = app.handle_user_exception(e)
            response = app.make_response(rv)
            return app.process_response(response)
        
        
app = Flask(__name__)

# Configure this environment variable via app.yaml
CLOUD_STORAGE_BUCKET = "superresolution_bucket_out"
#os.environ['CLOUD_STORAGE_BUCKET']

@app.route('/')
def index():
    return """
<form method="POST" action="/superres_upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
</form>
"""
def handler(request, response):
        return """
<form method="POST" action="/superres_upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
</form>
"""
    response.send({"message": "Successfully executed"})
