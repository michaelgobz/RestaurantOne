""" workspaces model"""

from datetime import datetime
from api.core.base import declarative_base as db


class Workspace(db.Model):
    """Workspace model"""

    __tablename__ = "workspaces"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tenant_id = db.Column(db.String(50), db.ForeignKey("tenants.id"))
    owner_id = db.Column(db.String(50), db.ForeignKey("users.id"))
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {"id": self.id, "name": self.name, "description": self.description}
