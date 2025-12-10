import re

#Patrón usuario
patron_usr = r"\w{1,25}"

#Patrón contraseña
patron_paswd = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

#Patrón confirmación contraseña
# patron_pasd2 = 

#Patrón mail

#USER
# user_input = input("Introduce tu usuario: ")
# verified_user = re.search(patron_usr,user_input)

# if verified_user != None:
#     print(verified_user.string, ": Usuario válido")
# else:
#     print(verified_user.string, ": Usuario no válido")

#PASSWORD

paswd_input = input("Introduce tu contraseña: ")
verified_paswd = re.search(patron_paswd,paswd_input)

if verified_paswd != None:
    print("Contraseña válida")
else:
    # print(verified_paswd.string, ": Contraseña no válida")
    print("Contraseña no válida")
