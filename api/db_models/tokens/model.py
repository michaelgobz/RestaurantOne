"""tokens model"""

from datetime import datetime

from api.core.base import declarative_base as db


class VerificationToken(db.Model):
    """VerificationToken model"""
    __tablename__ = 'verification_tokens'
    id = db.Column(db.String(50), primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'users.id'), nullable=False)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format
        """
        return {
            'id': self.id,
            'token': self.token,
            'created_at': self.created_at,
            'user_id': self.user_id

        }