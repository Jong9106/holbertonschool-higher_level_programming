#!/usr/bin/python3
""" script that changes the name of a State """

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).all()
    if states:
        states[0].name = "New Mexico"
    session.commit()
    session.close()
