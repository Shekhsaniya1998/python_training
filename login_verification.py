def login_verification(user_id,password):
    u_id=10
    passw=123
    if(u_id==user_id and password==passw):
        return True
    else:
        return False
print(login_verification(10,123))
