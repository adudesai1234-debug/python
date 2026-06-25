import bcrypt


password = input("enter your password: ")
ADMIN_PASS = "Admin@123"


def bcrypt_password(_Pass):
    a = bcrypt.hashpw(_pass,encode(), bcrypt gensalt())
    return a.decode()


    def check_pssword(_pass,_bcrypt):
      return bcrypt.checkpw(_pass.encode, _bcrypt_password)
      bcrypt.checkpw(_pass.encode, _bcrypt)