import protoblog as hello

my_list = hello.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"



first_item = hello.TodoListListItems()
first_item.state = hello.TaskState.TASK_DONE
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "31.10.2019"

my_list.todos.append(first_item)

print(my_list)
serialized = bytes(my_list)

print(serialized)

another = hello.TodoList().parse(serialized)
print(another.to_json(indent=2))
