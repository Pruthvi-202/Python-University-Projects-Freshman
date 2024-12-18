def passwordCheck(username, password, loginCredentials):
        if username in loginCredentials.keys():
            if loginCredentials[username] == password:
                return 'login successful'
            else:
                return 'login failed'
        else:
            return 'login failed'
