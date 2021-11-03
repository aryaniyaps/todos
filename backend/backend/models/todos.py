from backend import db


class Todo(db.Model):
    """Represents an user's todo."""

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

    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=db.func.now(),
        nullable=False,
    )

    __tablename__ = "todos"

    __mapper_args__ = {
        "order_by": created_at.desc()
    }

    def __repr__(self) -> str:
        return f"Todo <{self.content[:25]}>"
