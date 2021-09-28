from peewee import Model, PrimaryKeyField, DoesNotExist

from Core.database.db_connect import db


class BaseModel(Model):
	id = PrimaryKeyField(unique=True)

	@classmethod
	async def connect_DB(cls):
		db.connection().ping(reconnect=True)

	@classmethod
	async def get_by_id_or_none(cls, id):
		await cls.connect_DB()

		try:
			obj = cls.get(cls.id==id)
			db.close()
			return obj
		except DoesNotExist:
			db.close()
			return None

	@classmethod
	async def get_by_tg_id_or_none(cls, tg_id):
		await cls.connect_DB()

		try:
			obj = cls.get(cls.tg_id==tg_id)
			db.close()
			return obj
		except DoesNotExist:
			db.close()
			return None

	class Meta:
		database = db
		order_by = 'id'
