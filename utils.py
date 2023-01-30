
def order_data(users_db,users_file,users_permissions):
    arr = []
    for user_db in users_db:
        for user_file in users_file:
            for user_per in users_permissions:
                if str(user_db["_id"]) == user_file["id"] and str(user_db["_id"]) == user_per["id"]:
                    obj = {"id": user_file["id"],
                           "firstName": user_file["firstName"], "lastName": user_file["lastName"], "username": user_db["username"], "permissions": user_per["permissions"], "sessionTimeOut": user_file["sessionTimeOut"], "createdDate": user_file["createdDate"]}
                    if "admin" in user_file.keys():
                        obj["admin"] = True
                        arr.append(obj)
                    else:
                        arr.append(obj)
                    
    return arr
        
    

# def order_data(users_db,users_file):
#     arr = []
#     for user_db in users_db:
#         for user_file in users_file:
#             if str(user_db["_id"]) == user_file["id"]:
#                 obj={"id": user_file["id"], "name":user_file["firstName"]}
#                 arr.append(obj)
        
#     return arr
