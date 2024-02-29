from Database.mysqlConection import DBConnection, CorrectResultsModel
from CorrectResults.Domain.Entities.ACorrectResults import ACorrectResults as CorrectResultDomain
from CorrectResults.Domain.Entities.Type_status import Type_status

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
        
    def save(self, correct_domain: CorrectResultDomain):
        correct = CorrectResultsModel(
            valueRes=correct_domain.valueRes,
            correctResults_uuid=correct_domain.correctResults_uuid
        )
        self.session.add(correct)
        self.session.commit()
        return correct

    def list_all(self):
        correct = self.session.query(CorrectResultsModel).all()
        return correct
    
    def get_by_id(self, id):
        return self.session.query(CorrectResultsModel).filter(CorrectResultsModel.id == id).first()
    
    def update(self, id, correct_data):
        correct = self.get_by_id(id)
        correct.valueRes = Type_status[correct_data['valueRes']]
        self.session.commit()
        return correct
    
    def delete(self, id):
        correct = self.get_by_id(id)
        self.session.delete(correct)
        self.session.commit()
        return correct