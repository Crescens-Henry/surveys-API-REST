from Database.mysqlConection import DBConnection, UserModel
from User.Domain.Entities.User import User as UserDomain
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def save(self, usuario_dominio: UserDomain):
        usuario = UserModel(
            name=usuario_dominio.contact.name,
            last_name=usuario_dominio.contact.last_name,
            phone=str(usuario_dominio.contact.phone),
            email=usuario_dominio.credentials.email,
            password=usuario_dominio.credentials.password,
            user_uuid=usuario_dominio.user_uuid,
        )
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def getByEmail(self, email):
        usuario = self.session.query(UserModel).filter_by(email=email).first()
        return usuario
    
    def getByUuid(self, user_uuid):
        usuario = self.session.query(UserModel).filter_by(user_uuid=user_uuid).first()
        return usuario