from os import access
from flask import Blueprint, jsonify, request
from sqlalchemy import Identity
from werkzeug.security import check_password_hash,generate_password_hash

from src.constants import status_codes
import validators
from src.database import User, db
from flask_jwt_extended import create_access_token,create_refresh_token, get_jwt_identity,jwt_required


auth=Blueprint("auth",__name__, url_prefix="/api/v1/auth")

@auth.post("/register")
def register():
    username=request.json['username']
    email=request.json['email']
    password=request.json['password']


    if(len(password))<6:
        return  jsonify({"error":"password is too short"}),status_codes.HTTP_404_NOT_FOUND
    if(len(username))<6:
        return  jsonify({"error":"username is too short"}),status_codes.HTTP_404_NOT_FOUND
    # if "" in username:
    #     return jsonify({"error":"usernum should b allphanumeric"}),status_codes.HTTP_404_NOT_FOUND
    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}),status_codes.HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}),status_codes.HTTP_409_CONFLICT

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': "username is taken"}),status_codes.HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User created",
        'user': {
            'username': username, "email": email
        }

    }),status_codes.HTTP_201_CREATED

@auth.post("/login")
def login():
    email=request.json.get("email","")
    password=request.json.get("password","")
    user=User.query.filter_by(email=email).first()
    if(user):
        is_password_correct=check_password_hash(user.password,password)
        if(is_password_correct):
            if is_password_correct:
                refresh = create_refresh_token(identity=user.id)
                access = create_access_token(identity=user.id)

                return jsonify({
                    'user': {
                        'refresh': refresh,
                        'access': access,
                        'username': user.username,
                        'email': user.email
                    }
                    }),status_codes.HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}),status_codes.HTTP_401_UNAUTHORIZED

@auth.get("/me")
@jwt_required()
def me():
    user_id=get_jwt_identity()
    user=User.query.filter_by(id=user_id).first()
    return  jsonify({
        "username":user.username,
        "email": user.email
    }),status_codes.HTTP_200_OK
@auth.post("/token/refresh")
@jwt_required(refresh=True)
def refresh():
    identity=get_jwt_identity()
    access=create_access_token(identity=identity)
    return jsonify({
        "access":access
    }),status_codes.HTTP_200_OK

    
 

