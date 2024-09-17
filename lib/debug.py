from lib.db.models import Session, User, Category, Transaction

def debug():
    session = Session()

    # Add a new user
    new_user = User(username="tester")
    session.add(new_user)
    session.commit()

    print("User added:", new_user)

    session.close()

if __name__ == "__main__":
    debug()

