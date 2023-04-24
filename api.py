from flask import Blueprint, request, make_response, redirect, url_for, request_finished
from flask_cors import CORS, cross_origin
import sys, os, time, mariadb
import json

from .db import conn, cur


views = Blueprint('views', __name__)

@views.route('/inject/', methods=['POST'])
@cross_origin()
def inject():
    pass

@views.route('/obtain', methods=["GET"])
@cross_origin()
def obtain():
    if request.method == 'GET':
        #puts the request args into a dict(key-val)
        args = request.args.to_dict()
        #grabs intormation from the database
        conn
        cur.execute("SELECT _ FROM _")
        data = cur.fetchall()
        #formats data into json format
        row_headers=[x[0] for x in cur.description]
        json_data = []
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        if args:
            #declares filter class and provides the data
            json_filter = JsonFilter(json_data)
            #defines arguments, and assigns the filter to a list
            filtered_array = json_filter.filter(args)
            resp = make_response(filtered_array)
        elif not args:
            resp = make_response(json_data)
        #return the responses
        return resp    
