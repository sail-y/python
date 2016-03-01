# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# deque  双向链表

from collections import deque

q = deque(['a', 'b', 'c'])

q.append('x')
q.appendleft('y')

print(q)

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
print(dd['hello'])

# OrderedDict

from collections import OrderedDict

od = OrderedDict([('a', 1), ('d', 2), ('c', 3)])
print(list(od.keys()))

# Counter

from collections import Counter

c = Counter()
for ch in 'hellocounter':
    c[ch] += 1
print(c)
