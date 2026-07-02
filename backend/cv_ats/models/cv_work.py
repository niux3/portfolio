from datetime import datetime
from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class CvWork(db.Model, SerializerMixin):
    __tablename__ = 'cv_works'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128), nullable=False)
    year_start = db.Column(db.SmallInteger, nullable=True)
    year_end = db.Column(db.SmallInteger, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    position_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'cv_positions.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        nullable=False
    )
    position = db.relationship("CvPosition", backref="cv_works")

    contract_type_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'cv_contracts.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        nullable=False
    )
    contract_type = db.relationship("CvContractType", backref="cv_works")

    customers_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'project_customers.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        nullable=False
    )
    customer = db.relationship("Customer", backref="cv_works")

    def __str__(self):
        if self.year_start and self.year_start != self.year_end:
            return f"{self.customer.name} ({self.year_start} - {self.year_end})"
        return f"{self.customer.name} ({self.year_end})"

    def __repr__(self):
        if self.year_start and self.year_start != self.year_end:
            return f"<CvWork {self.customer.name} {self.year_start} - {self.year_end}>"
        return f"<CvWork {self.customer.name} {self.year_end}>"