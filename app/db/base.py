from sqlalchemy.orm import declarative_base
Base = declarative_base()


from app.db.models import user_model
from app.db.models import habit_model
from app.db.models import subscription_model
from app.db.models import diary_model
from app.db.models import habit_log_model