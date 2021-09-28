from core.Base.BaseRedis import BaseRedis


class UserRedis(BaseRedis):

	async def redis_save(self):
		self.redis.set('redis_data', 'data')

	async def redis_get(self):
		return self.redis.get('redis_data')

	async def redis_delete(self):
		self.redis.delete('redis_data')
		