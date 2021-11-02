from backend import db


class Todo(db.Model):
    """Represents an user's todo."""

    __tablename__ = "todos"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    content = db.Column(
        db.Text,
        nullable=False,
    )

    completed = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        nullable=False,
    )

    updated_at: db.Column(
        db.DateTime(timezone=True),
        onupdate=db.func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"Todo <{self.content[:25]}>"
