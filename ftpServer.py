from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
# Définition de l'utilisateur et du mot de passe
user = "epsi"
password = "client22"

class MyHandler(FTPHandler):
    # Définition de l'utilisateur et du mot de passe pour la connexion au serveur
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, ".", perm="elradfmwMT")

handler = MyHandler
handler.passive_ports = range(60000, 65535)

# Création du serveur
address = ("127.0.0.1", 21) # 21 est le port FTP par défaut
server = FTPServer(address, handler)

# Démarrage du serveur
server.serve_forever()

# Modification du mot de passe de l'utilisateur epsi
authorizer = server.handler.authorizer
authorizer.update_user("epsi", "badr", ".")