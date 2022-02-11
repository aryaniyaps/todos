"""add todos

Revision ID: 5979d11c46f8
Revises: dee7e2b6f04d
Create Date: 2022-01-23 18:32:57.082549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5979d11c46f8'
down_revision = 'dee7e2b6f04d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", "user_id"),
    )


def downgrade():
    op.drop_table("todos")
