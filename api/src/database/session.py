from sqlalchemy.orm import Session, sessionmaker

from .engine import engine

LocalSession = sessionmaker(bind=engine)


def session_manager(auto_commit=True) -> Session:
    """ Provide a transactional scope around a series of operations. """
    session = LocalSession()

    try:
        yield session

        if auto_commit:
            session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
