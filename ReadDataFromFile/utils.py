# Utils lib written in python for learning.
import random
from datetime import date, datetime, timedelta
class CustomUtils:
    
    def yesish(self, value):
        return str(value).strip().lower() in ["true", "yes", "y", "1"]

    def noish(self, value):
        return str(value).strip().lower() in ["false", "no", "n", "0"]

    def randomInt(self, max=5, min= 1):
        return  random.randint(min, max)

        # Combine an array of objects of arrays into a single object
        # with concatenated arrays.
        #   x = a: [1, 2], b: [3, 4]
        #   y = b: [5, 6], c: [7, 8]
        #   z = Fn::Combine [x, y]
        #   // z is a: [1, 2], b: [3, 4, 5, 6], c: [7, 8]

    def combineArrays(self, source):
        result = {}
        for i in source:
            print("intem in source", i)
            for k,v in i.items():
                print("k", k)
                print("v", v)
                try:
                    result[k].extend(v)
                    print("after append", result)
                except KeyError as e:
                    result[k] = v
                    print("got error ", e)
        return result

    # Check if the given timestamp will expire?.
    def will_expire(self, timestamp, age):
        now_time = datetime.now()
        ts = datetime.strptime(timestamp, '%d/%m/%y %H:%M:%S')
        delta = now_time - ts
        print("now -----> ", now_time)
        print("ts -----> ", ts)
        print(delta)
        return True
        


c = CustomUtils()
print(c.yesish(4))
print(c.yesish("yes"))
print(c.randomInt())
print(c.combineArrays([{"a":[1, 2, 2, 3443]}, {"a": [5], "b": "foo"}]))

print(c.will_expire("18/09/19 01:55:19", 3))