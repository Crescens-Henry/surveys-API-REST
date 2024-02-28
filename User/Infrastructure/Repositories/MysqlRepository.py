from Database.mysqlConection import DBConnection, UserModel
from User.Domain.Entities.AUser import User as UserDomain
class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def save(self, usuario_dominio: UserDomain):
        user = UserModel(
            name=usuario_dominio.contact.name,
            last_name=usuario_dominio.contact.last_name,
            phone=str(usuario_dominio.contact.phone),
            email=usuario_dominio.credentials.email,
            password=usuario_dominio.credentials.password,
            user_uuid=usuario_dominio.user_uuid,
            type=usuario_dominio.type.name
        )
        self.session.add(user)
        self.session.commit()
        return user

    def getAll(self):
        user = self.session.query(UserModel).all()
        return user
    
    def get_by_id(self, id):
        return self.session.query(UserModel).filter(UserModel.id == id).first()
    
    def getByEmail(self, email):
        user = self.session.query(UserModel).filter_by(email=email).first()
        return user
    
    def getByUuid(self, user_uuid):
        user = self.session.query(UserModel).filter_by(user_uuid=user_uuid).first()
        return user
    
    def update(self, id, user_data):
        user = self.get_by_id(id)
        user.name = user_data['name']
        user.last_name = user_data['last_name']
        user.phone = user_data['phone']
        user.email = user_data['email']
        user.password = user_data['password']
        user.type = user_data['type']
        self.session.commit()
        return user
    
    def delete(self, id):
        user = self.get_by_id(id)
        self.session.delete(user)
        self.session.commit()
        return user