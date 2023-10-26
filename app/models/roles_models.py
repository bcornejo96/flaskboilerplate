from app.models import BaseModel
from sqlalchemy import Column, Integer, VARCHAR, Boolean

class RoleModel(BaseModel):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(8))
    status = Column(Boolean, default=True)