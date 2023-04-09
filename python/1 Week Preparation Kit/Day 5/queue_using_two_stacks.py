q = int(input())
stack_push = []
stack_delete = []

for i in range(q):
    input_row = list(input().split())

    # enqueue
    if input_row[0] == '1':
        stack_push.append(input_row[1])


    # dequeue
    elif input_row[0] == '2':
        if not stack_delete:
            while stack_push:
                stack_delete.append(stack_push.pop())
        stack_delete.pop()

    # print
    else:
        if not stack_delete:
            while stack_push:
                stack_delete.append(stack_push.pop())

        print(stack_delete[-1])
