from peewee import CharField

from core.database.BaseModel import BaseModel


class UserModel(BaseModel):
	tg_id = CharField()

	class Meta:
		db_table = 'users'
