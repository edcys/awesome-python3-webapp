import orm, asyncio
from models import User, Blog, Comment

async def test():
    await orm.create_pool(loop=loop, user='sb', password='sb', db='awesome')

    u = User(name='Test8', email='test8@example.com', passwd='1234567890', image='about:blank')

    await u.save()

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())