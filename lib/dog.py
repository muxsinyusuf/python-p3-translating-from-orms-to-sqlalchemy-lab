from models import Dog

def create_table(base):
   busy =Dog(
       name = "busy",
       breed = 'american'

   )
     
  

def save(session,busy):
    session.add(busy)
    session.commit()

  

def get_all(session):
   dog_name=session.query(Dog.name).all()
   print(dog_name)

def find_by_name(session, name):
    query = session.querry(Dog).filter(name.like('%busy%'),)
    

def find_by_id(session, id):
        query = session.querry(Dog).filter(id)

   

def find_by_name_and_breed(session, name, breed):
        query = session.querry(Dog).filter(name.like('%busy%'),breed)

    

def update_breed(session, dog, breed):
    session.query(Dog).update({
         dog: breed+1
    })

    pass