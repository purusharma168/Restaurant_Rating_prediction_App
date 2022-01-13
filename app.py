import logging
import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)