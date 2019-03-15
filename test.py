from cola import Cola
queue = Cola()

queue.put('Hola')
queue.put('que')
queue.put('hace')
print(queue.isEmpty())
print(queue.items)
print(queue.size())
queue.get()
print(queue.items)
print(queue.size())
queue.get()
queue.get()
print(queue.isEmpty())

