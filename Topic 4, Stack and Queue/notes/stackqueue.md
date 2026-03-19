## Stack and Queue:

# What is a Stack?
The simplest explanation of the data structure Stack is its a linear type of data structure which follows a specific pattern which commonly is called:

- LIFO -> and its full form is last in first out.
for this the common example could be anything which is placed/stacked upon each other like for example:

. number of boxes are placed on each other, now when the new box is to be added it is simply placed on the top of the existing boxes. 

. now when the condition or desire is to remove the box then it is simlpy removed from the top of boxes, so this is what the basic workflow of the lifo -? last in first out data structure is.

# Some Basic Operations:
- now some main operations which are performed in the lifo data structure are:
. push(x) -> this operation means adding the given element to the top,
. pop() -> this operation means removing the given element from the top,
. peek() / top() -> this operation means to be able to see like which given element is present on top.
. is_empty() -> this operation means checking like whether the storage of the data is empty or not?

# code example operations of stack using the list:
1. 
stack = []

stack.append(5)
stack.append(10)

now these two above lines means add these two numbers which are 5 and 10 in the list. and this process is called the push operation.

2. 
stack.pop()  

now this line means as according to the above given list in which the numbers 5 and 10 were added, now from that list remove a number and that removing of a number opeation is simply called a pop opration.
. so here which ever number was added last actually which is number 10 so first it will be removed/popped from the list.

3. 
Now the third opeartion here is peek operation which we talked earlier means to be able to see the top of the given data structure being used for data storage like in current example the list is that one.

4. 
And lastly another check which is possible here is the empty check. Like whether the given list for example in this case has any element or not? 
. So if its empty then this operation will show the empty result according to this operation.
- Key point:
The data structure of lists which is used in the python it follows the stack like flow.

# What is a Queue?
Now if we talk about the understanding of the queue then like stacks used the lifo structure od data flow so in queues,

the structure of the FIFO is used -> and it is commonly called as the first in first out.

now here the common example of this fifo could be explained as,
a line of persons present anywhere like on road, shop, outside the atm, bank, clerk office, etc.

- so according to the basic principles whoever is the first person present -> that person is going to be served first before the other, and just like that this whole process will continue.

- Some common operations in queue:
. enqueue(x) -> this operation means the addition of a element at the end or say at the back of the queue for example.
. dequeue() -> this operation means to be able to remove from front, like remove the element from the front.
. front() -> this operation means to see the first present element

- code example of queue:
queue = []
queue.append(5)
queue.append(10)
. now here this way of addition for exam of the two numbers in the list named queued is commonly called enqueueing, menas addition of the new values inside the list/queue.

queue.pop(0)
. now here this above code line is removing the number present at the index 0, and this way of value removal in the queue is called as dequeueing.

# The Imp Use cases of Stack and Queue:
- The use of Stack is common:
. In Function calls -> in the call of stack is used,
. In Undo/Redo operations,
. In the analyis/evaluation of the expression,
. And in the process of backtracking -> which is related to the depth first search (DFS).

- The use of Queue is common:
. In the scheduling of the task,
. In the Breadth First Search (BFS),
. And also in the processes of handling the requests.

# What is Monotonic Stack?
The concept of a monotonic tack tells its a kind of stack in which the present elements are placed in the specific order and these ordes are:
. Increasing stack,
. Decreasing stack

1. Increasing Stack:
. The increasing stack is the type of stack which keeps the present smallest elements at the bottom point.
. Also these are used in the cases of finding the next smaller element.

2. Decreasing Stack:
. The decreasing stack is the type of stack which keeps the present largest elements at the bottom point.
. And these are used in the cases of finding the next greater element.