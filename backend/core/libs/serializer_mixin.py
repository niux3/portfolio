from backend import db
from datetime import datetime


class SerializerMixin:
    def to_dict(self):
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, datetime):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
        return result

    @classmethod
    def from_dict(cls, data):
        # On filtre pour ne prendre que les colonnes de la table
        filtered_data = {}
        for column in cls.__table__.columns:
            key = column.name
            if key in data:
                value = data[key]
                # Si la colonne est un datetime, on convertit
                if isinstance(column.type, db.DateTime) and value is not None:
                    try:
                        value = datetime.fromisoformat(value)
                    except Exception:
                        pass
                filtered_data[key] = value
        return cls(**filtered_data)
