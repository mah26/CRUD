# ORM Mock
class Film():
  def __init__(self, id, title, category, length):
    self.id = id
    self.title = title
    self.category = category
    self.length = length


  def json(self):
    return { 'id': self.id, 'title': self.title, 'lenght': self.length, 'category':self.category}


  @staticmethod
  def get_by_id(id):
    return Film(1, 'El resplandor', 'Terror', 140)

  @staticmethod
  def get_all():
    return [ Film(1, 'El resplandor', 'Terror', 140), Film(2, 'IT', 'Terror', 90)]

  def create(self):
    #Logic that saves the data in DataBase
    return self

      
  def update(id):
    #Logic
    return self 

    
  def delete(self):
    return self
