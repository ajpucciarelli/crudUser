from model.user import User
from dao.engine import session

def commit_close(func):
    def decorator(*args):
        with sessionmaker(engine) as session:
            try:
                func(*args)
            except:
                session.rollback()
                raise
            else:
                session.commit()
    return decorator

@commit_close
def db_insert(name, phone, email):
    print('db_insert()')
    usuario = User(name=name, phone=phone, email=email)  
    session.add(usuario)

@commit_close
def db_update(name, email):
    usuarios = db_select(email, 'email')
    for usuario in usuarios:
        usuario.name = name

@commit_close
def db_delete(email):
    session.query(User).filter(User.email==email).delete()

def db_selectAll():
    print('db_selectAll()')
    results = session.query(User).all()
    return results

def db_select(data, field):
    print('db_select()')
    results = session.query(User).filter(getattr(User, field).like("%%%s%%" % data)).all()
    return results