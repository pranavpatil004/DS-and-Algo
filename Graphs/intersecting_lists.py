# You are given a collection of singly-linked lists (SLLs). Return true if any of them share a common node (or “intersect”), or false otherwise. Please don’t use recursion. Assume the SLLs might be very large in length (in the millions). Stop traversing and return immediately if you detect a common node. If a cycle is detected, please throw an error. Aim to be as efficient as possible from a time complexity perspective.

# Implement this function with this signature:

# DoLinkedListsIntersect(Collection<SinglyLinkedList>) returns bool

# Input:
# Your program should read lines of text from the standard input in Codevue. The first lines of the input will describe the singly-linked-lists in a directed acyclic graph (DAG) format. The graph description language is a similar idea to the GraphViz graph description language, see: https://en.wikipedia.org/wiki/DOT_(graph_description_language).

# Each node is described as a string token, which is a unique identifier for the node. So “a->b” means a DAG with node “a” directionally connected to node “b”. As we are describing singly-linked-lists, take it as a given that the out degree of every node is either zero or one.

# After each of the edges has been described, then each subsequent line will include set of SLL starting nodes to traverse from. We advise that you draw a diagram to help you understand the example more clearly.

# Note: we have added an attachment image to show this visually.

# Output:
# For each SLL print true or false based on whether any of the traversals intersect, which is to say, whether they share a common node.

# Test 1
# Test Input
# Download Test 1 Input
# a->b
# r->s
# b->c
# c->a
# x->c
# q->r
# y->x
# w->z
# a,q,w
# a,c,r
# y,z,a,r
# a,w
# Expected Output
# Download Test 1 Output
# False
# True
# True
# False
# Test 2
# Test Input
# Download Test 2 Input
# A->B
# G->B
# B->C
# C->D
# D->E
# H->J
# J->F
# A,G,E
# H,A
# Expected Output
# Download Test 2 Output
# True
# False

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev_nodes = set()

class Solution:
    def __init__(self) -> None:
        self.created_nodes = {}

    def get_node(self, data):
        if data in self.created_nodes:
            node = self.created_nodes[data]
        else:
            node = Node(data)
            self.created_nodes[data] = node
        return node
    
    def start(self, arr):
        for string in arr:
            if "->" in string:
                nodes = string.split("->")
                first_node = self.get_node(nodes[0].strip())
                second_node = self.get_node(nodes[1].strip())
                if first_node.next:
                    raise Exception("More than one outward connection for a node")
                first_node.next = second_node
                second_node.prev_nodes.update(first_node.prev_nodes)
                if second_node.data in first_node.prev_nodes:
                    raise Exception("Cycle detected in the system")
                second_node.prev_nodes.add(first_node.data)
                first_node.prev_nodes = set()
            else:
                heads = string.split(",")
                visited_nodes = set()
                is_intersection_found = False
                for head_data in heads:
                    head = self.created_nodes[head_data.strip()]
                    while head:
                        if head in visited_nodes:
                            is_intersection_found = True
                            break
                        visited_nodes.add(head)
                        head = head.next
                    else:
                        continue
                    break
                print(str(is_intersection_found))




# arr = [
# "a->b",
# "r->s",
# "b->c",
# "x->c",
# "q->r",
# "y->x",
# "w->z",
# "a,q,w",
# "a,c,r",
# "y,z,a,r",
# "a,w"
# ]


arr = ["A->B",
"G->B",
"B->C",
"C->D",
"D->E",
"H->J",
"J->F",
"A,G,E",
"H,A", "A,C", "B"]
Solution().start(arr)
