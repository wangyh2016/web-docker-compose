from flask import Flask
import redis
import time


app = Flask(__name__)
cache = redis.Redis(host='myredis',port=6379)


def get_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as exc:
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.3)

	
@app.route('/')

def hello():

	cnt = get_count()
	return 'hello world! cnt={}\n'.format(cnt)



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
