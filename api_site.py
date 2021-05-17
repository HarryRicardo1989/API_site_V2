#!/usr/bin/python3
from flask import Flask, render_template, request, json
from convert_to_json import JsonAda
app = Flask(__name__)
import os


@app.route('/passagens')
def passagens():
    return JsonAda().json_passagens()


@app.route('/status')
def status():
    return JsonAda().json_status()


@app.route('/statusSistema')
def status_completo():
    return JsonAda().json_completo()


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)



  