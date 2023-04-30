from flask import Blueprint, request, make_response, redirect, url_for, request_finished
from flask_cors import CORS, cross_origin
import sys, os, time, mariadb
import json

from .db import testdb, betadb


enpoints = Blueprint('endpoints', __name__)

@enpoints.route('/inject-weapon/', methods=['POST'])
@cross_origin()
#allows whichever api user to inject a weapon into the weapons database
def injectWeapon():
    collection = testdb['weapon_types']
    try:
        weapon = request.args('weaponName')
        attachments = request.args('attachments')
        



@endpoints.route('/obtain', methods=["GET"])
def obtain():
    pass



@endpoints.route('/update', methods=["GET"])
def update():
    pass
