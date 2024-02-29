from Database.mysqlConection import DBConnection, ResultsModel
from Results.Domain.Entities.AResult import AResult as ResultDomain
from Results.Domain.Entities.Result import Result

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
        
    def save(self, result_domain: ResultDomain):
        result = ResultsModel(
            result=result_domain.result,
            statusResult=result_domain.statusResult,
            result_uuid=result_domain.result_uuid
        )
        self.session.add(result)
        self.session.commit()
        return result

    def list_all(self):
        result = self.session.query(ResultsModel).all()
        return result
    
    def get_by_id(self, id):
        return self.session.query(ResultsModel).filter(ResultsModel.id == id).first()
    
    def update(self, id, result_data):
        result = self.get_by_id(id)
        result.result = Result[result_data['result']]
        result.statusResult = result_data['statusResult']
        self.session.commit()
        return result
    
    def delete(self, id):
        result = self.get_by_id(id)
        self.session.delete(result)
        self.session.commit()
        return result