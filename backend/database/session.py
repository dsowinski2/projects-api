from contextlib import contextmanager

from sqlalchemy import orm

from .connection import db

Session = None

if db is not None:
    Session = orm.scoped_session(orm.sessionmaker())
    Session.configure(bind=db)


def db_session() -> Session:
    session = Session()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


db_context = contextmanager(db_session)
session = next(db_session())
