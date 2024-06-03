"""description of changes\

Revision ID: 387a0d1cd5c0
Revises: 
Create Date: 2024-06-02 17:48:11.262422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '387a0d1cd5c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_reviews')
    op.drop_table('course_review_stats')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_review_stats',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('course_id', sa.VARCHAR(length=100), nullable=False),
    sa.Column('easy_count', sa.INTEGER(), nullable=True),
    sa.Column('medium_count', sa.INTEGER(), nullable=True),
    sa.Column('hard_count', sa.INTEGER(), nullable=True),
    sa.Column('homework_less', sa.INTEGER(), nullable=True),
    sa.Column('homework_medium', sa.INTEGER(), nullable=True),
    sa.Column('homework_more', sa.INTEGER(), nullable=True),
    sa.Column('grading_low', sa.INTEGER(), nullable=True),
    sa.Column('grading_medium', sa.INTEGER(), nullable=True),
    sa.Column('grading_high', sa.INTEGER(), nullable=True),
    sa.Column('harvest_low', sa.INTEGER(), nullable=True),
    sa.Column('harvest_medium', sa.INTEGER(), nullable=True),
    sa.Column('harvest_high', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('course_id')
    )
    op.create_table('course_reviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('course_id', sa.VARCHAR(length=100), nullable=True),
    sa.Column('rating', sa.FLOAT(), nullable=True),
    sa.Column('ratingCount', sa.INTEGER(), nullable=True),
    sa.Column('difficulty', sa.VARCHAR(length=50), nullable=True),
    sa.Column('homework', sa.VARCHAR(length=50), nullable=True),
    sa.Column('grading', sa.VARCHAR(length=50), nullable=True),
    sa.Column('harvest', sa.VARCHAR(length=50), nullable=True),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.Column('created_time', sa.DATETIME(), nullable=True),
    sa.Column('last_updated_time', sa.DATETIME(), nullable=True),
    sa.Column('student_id', sa.VARCHAR(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
