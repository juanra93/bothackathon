from pony.orm import *
from ucobot.model import db

class User(db.Entity):
    """Clase User.
    Representa a un usuario de Telegram.
    """
    id = PrimaryKey(int, auto=False)
    first_name = Optional(str, nullable=True)
    last_name = Optional(str, nullable=True)
    username = Optional(str, nullable=True)
    votos = Set("Voto")

class Chica(db.Entity):
    id = PrimaryKey(int, auto=True)
    votos = Set("Voto")

class Voto(db.Entity):
    voto = Required(int)
    user = Required(User)
    chica = Required(Chica)

@db_session
def search_user(user):
    """
    Busca y devuelve un usuario en la base de datos. Si no existe lo crea.
    """
    if select(u for u in User).filter(lambda x: x.id == user.id).exists():
        entity = User[user.id]
        entity.first_name = user.first_name
        entity.last_name = user.last_name
        entity.username = user.username
    else:
        entity = User(id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)
        commit()

    return entity

@db_session
def search_chica(chica):
    """
    Busca y devuelve un usuario en la base de datos. Si no existe lo crea.
    """
    if select(u for u in Chica).filter(lambda x: x.id == chica).exists():
        entity = Chica[chica]
    else:
        entity = Chica(id=chica)
        commit()

    return entity

@db_session
def guardar_voto(usuario, chica, nota):
    usuario = search_user(usuario)
    chica = search_chica(chica)

    Voto(user=usuario, chica=chica, voto=nota)
    commit()

