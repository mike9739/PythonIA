import Queue

q = Queue.Queue()

q.put(5)
print(q.get())
# print(q.empty())
# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get())

print('First item')
print(q.get())
print('finish')