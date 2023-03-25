from flask import Blueprint, request, make_response, redirect, url_for, request_finished
from flask_cors import CORS, cross_origin
import sys, os, time, mariadb
import json

views = Blueprint('views', __name__)

@views.route('/inject/', methods=['POST'])
@cross_origin()
def inject():
    pass