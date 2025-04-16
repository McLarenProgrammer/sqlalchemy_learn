from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

postgre_engine = create_engine(
    "postgresql+psycopg://rec-user:27099123zb@localhost:5432/recommendationsystem",
    echo=True
)

with Session(postgre_engine) as session:
    result = session.execute(
        text("UPDATE users SET is_cataloger=:isCataloger WHERE login=:login"),
        [{"isCataloger": False, "login": "TUTUNKIN_MD"}, {"isCataloger": True, "login": "KURNOSOV_VP"}]
    )
    session.commit()