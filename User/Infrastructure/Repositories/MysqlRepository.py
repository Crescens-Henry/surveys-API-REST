from Database.mysqlConection import DBConnection, User
from User.Domain.Entities.User import User as UserDomain
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def guardar(self, usuario_dominio: UserDomain):
        usuario = User(
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

    def obtener_todos(self):
        return self.session.query(User).all()

    def obtener(self, user_id: str):
        usuario = self.session.query(User).get(user_id)
        return usuario

    def actualizar(self, user_id: str, contact: Contact, credentials: Credentials):
        usuario = self.session.query(User).get(user_id)
        if usuario:
            usuario.name = contact.name
            usuario.last_name = contact.last_name
            usuario.phone = str(contact.phone)
            usuario.email = credentials.email
            usuario.password = credentials.password
            self.session.commit()
            self.session.refresh(usuario)
        return usuario

    def eliminar(self, user_id: str):
        usuario = self.session.query(User).get(user_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False

    def obtener_por_email(self, email):
        usuario = self.session.query(User).filter_by(email=email).first()
        return usuario
    
    def obtener_por_uuid(self, user_uuid):
        usuario = self.session.query(User).filter_by(user_uuid=user_uuid).first()
        return usuario

    def verificar_usuario(self, user_uuid):
        try:
            usuario = self.session.query(User).filter_by(user_uuid=user_uuid).one()
            self.session.query(User).filter_by(id=usuario.id).update({User.verified: True})
            self.session.commit()
            return usuario
        except:
            print ("Error")
            return None