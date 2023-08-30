"""empty message

Revision ID: 296695df1c37
Revises: 
Create Date: 2023-08-29 12:40:44.378801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '296695df1c37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('roadmaps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roadmap_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['roadmap_id'], ['roadmaps.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('roadmap_id', sa.Integer(), nullable=False),
    sa.Column('parent_step_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_step_id'], ['steps.id'], ),
    sa.ForeignKeyConstraint(['roadmap_id'], ['roadmaps.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('step_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['step_id'], ['steps.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('roadmap_id', sa.Integer(), nullable=False),
    sa.Column('current_step_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['current_step_id'], ['steps.id'], ),
    sa.ForeignKeyConstraint(['roadmap_id'], ['roadmaps.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('progress')
    op.drop_table('posts')
    op.drop_table('steps')
    op.drop_table('categories')
    op.drop_table('roadmaps')
    op.drop_table('users')
    # ### end Alembic commands ###