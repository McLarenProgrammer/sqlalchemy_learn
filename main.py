from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

postgre_engine = create_engine(
    "postgresql+psycopg://rec-user:27099123zb@localhost:5432/recommendationsystem",
    echo=True
)

stmt = text("SELECT login, password_hash, is_cataloger FROM users WHERE is_cataloger = :isCataloger")
with Session(postgre_engine) as session:
    result = session.execute(stmt, {"isCataloger": True})
    for row in result:
        print(f"Login: {row.login} Password_hash: {row.password_hash} Cataloger: {row.is_cataloger}")