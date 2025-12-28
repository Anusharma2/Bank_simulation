import gmail
def send_credentials(email,name,acn,pwd):
    con=gmail.GMail('anuu.sharma309@gmail.com','12345678')
    body=f'''Hello {name},
    Welcome to ABC Bank,here is your crendentials
    Account No = {acn}
    Password = {pwd}

    Kindly change your password when you login first time
    
    ABC Bank
    Sector-16, Noida
'''
    msg=gmail.Message(to=email,subject='Your Credentials for operating account',text=body)
    con.send(msg)


def send_otp(email,name,otp):
    con=gmail.GMail('anuu.sharma309@gmail.com','lrbx ohpa ndzq jxhk')
    body=f'''Hello {name},
    Welcome to ABC Bank,here is your otp to recover password
    
    OTP={otp}

    ABC Bank
    Sector-16, Noida
'''
    msg=gmail.Message(to=email,subject='OTP for password recovery',text=body)
    con.send(msg)


def send_otp_withdraw(email,name,otp,amt):
    con=gmail.GMail('anuu.sharma309@gmail.com','lrbx ohpa ndzq jxhk')
    body=f'''Hello {name},
    Welcome to ABC Bank,here is your otp to withdraw amount of Rs.{amt}
    
    OTP={otp}

    ABC Bank
    Sector-16, Noida
'''
    msg=gmail.Message(to=email,subject='OTP for withdraw',text=body)
    con.send(msg)

def send_otp_transfer(email,name,otp,amt,to_acn):
    con=gmail.GMail('anuu.sharma309@gmail.com','lrbx ohpa ndzq jxhk')
    body=f'''Hello {name},
    Welcome to ABC Bank,here is your otp to transfer amount of Rs.{amt} to ACN:{to_acn}

    
    OTP={otp}

    ABC Bank
    Sector-16, Noida
'''
    msg=gmail.Message(to=email,subject='OTP for transfer',text=body)
    con.send(msg)
