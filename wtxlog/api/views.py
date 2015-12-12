# -*- coding: utf-8 -*-

from flask import request, jsonify
from ..models import db, Article,Apply,User
from . import api


@api.route('/gethits/')
def gethits():
    id = int(request.args.get('id', 0))
    article = Article.query.get(id)
    if article:
        article.hits += 1
        db.session.add(article)
        db.session.commit()
        return str(article.hits)
    return 'err'


@api.route("/applys/<int:userid>")
def applys(userid=1):
    num_results = int(request.args.get("num_results", 20))

    if num_results > 100:
        num_results = 100

    applys = Apply.query.latestforuser(userid).limit(num_results)

    return jsonify(results=list(applys.jsonify()))

@api.route("/addapply", methods=("GET", "POST"))
def addapply():

    apply = Apply(title=request.form.get("title", None),reason=request.form.get("reason", None),\
        applyer_id=request.form.get("applyer_id", None))
    db.session.add(apply)
    db.session.commit()

    return jsonify(success=True)

@api.route("/approval", methods=("GET", "POST"))
def approval():

    Apply.approval()
    db.session.commit()

    return jsonify(success=True)

@api.route("/allusers", methods=("GET", "POST"))
def allusers():
    num_results = int(request.args.get("num_results", 20))

    if num_results > 100:
        num_results = 100
    users = User.query.get_all()
    print(users)

#    return jsonify(results=users)
    return jsonify(results=list(users.jsonify()))
