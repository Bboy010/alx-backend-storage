# REDIS BASIC
``` Redis is just a fancy hash table ```
---

### Tasks 0

[0.Writing strings to Redis](0x02-redis_basic/exercise.py)

1. Create a Cache class.
2. Create a store method that takes a data argument and returns a string.
3. Create a get method that takes a key string argument and returns a value.

### Tasks 1

[1. Reading from Redis and recovering original type](0x02-redis_basic/exercise.py)
1. Create a get method that takes a key string argument and an optional Callable argument fn and returns a value.
2. conserve the original Redis.get behavior if the key does not exist in Redis.
3. implement 2 new methods: get_str and get_int.
4. get_str and get_int will automatically parametrize Cache.get to return the data as the desired type.

### Tasks 2

[2. Incrementing values](0x02-redis_basic/exercise.py)
1. Implement a system to count how many times methods of the Cache class are called.
2. Create and return function that increments the count of that key every time the method is called and returns the value returned by the original method.

### Tasks 3

[3. Storing lists](0x02-redis_basic/exercise.py)
```Familiarize yourself with redis commands RPUSH, LPUSH, LRANGE, etc.```
1. Implement a ```call_history``` decorator to store the history of inputs and outputs for a particular function.
2. In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.
3. call_history has a single parameter named method that is a Callable and returns a Callable.
4. use rpush to append the input arguments to the input key.

### Tasks 4

[4. Retrieving lists](0x02-redis_basic/exercise.py)
1. Implement a ```replay``` function to display the history of calls of a particular function.

### Tasks 5

[5. Implementing an expiring web cache and tracker](0x02-redis_basic/exercise.py)
1. Implement a get_page function ```(prototype: def get_page(url: str) -> str:).``` 
2. Use the requests module to obtain the HTML content of a particular URL and return it.
3. Cache the result for 10 seconds using ```redis.setex```.
4. Tip: Use [robertomurray](http://slowwly.robertomurray.co.uk) to simulate a slow response and test your caching.

---
💘 Redis Basic 💘
