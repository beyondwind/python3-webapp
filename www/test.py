import orm,asyncio
from models import User

def test(loop):
	yield from orm.create_pool(loop=loop,user='root',password='root',db='mydb')
	u=User(name='test',email='test@dsa.com',passwd='123456',image='about:blank')
	yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()