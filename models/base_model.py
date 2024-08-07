import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id, name,updated_at=None,created_at=None):
        self.id= str(uuid.uuid4())
        self.name= name
        self.updated_at=datetime.now()
        self.created_at=datetime.now()
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__)
    def save(self):
        self.updated_at=datetime.now()
    def to_dict(self):
        my_dict=self.__dict__.copy()
        my_dict["__class__"]=self.__class__.__name__
        my_dict["created_at"]=my_dict["created_at"].isoformat()
        my_dict["updated_at"]=my_dict["updated_at"].isoformat()
        

        return my_dict

  
