from collections import defaultdict
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        # print(A)
        tree = defaultdict(dict)
        for row in A:
            tree[min(row[:2])][max(row[:2])] = row[2]
        cache = {}
        def get_path(root, B, stack):
            if root == B:
                return True
            
            for ele in tree[root].keys():
                stack.append(ele)
                found = get_path(ele, B, stack)
                if found:
                    return True
                stack.pop()
        
        def get_max_edge_in_subtree(source, destination):
            if not tree[source]:
                return 0, False
            if (source, destination) in cache:
                return cache[(source, destination)], True if cache[(source, destination)] > 0 else False
            max_edge = 0
            print("test", tree[source].keys())
            for ele in tree[source].keys():
                if ele == destination:
                    max_edge = max(max_edge, tree[source][destination])
                    return max_edge, True
                edge, found = get_max_edge_in_subtree(ele, destination)
                if found:
                    max_edge = max(max_edge, edge)
                    cache[(source, destination)] = max_edge
                    return max_edge, True
            return 0, False
        
        def get_max_edge_in_stack(source, destination, stack):
            # print(source, destination, "source")
            if (source, destination) in cache:
                return cache[(source, destination)]
            prev = stack.pop()
            found = False
            max_edge = 0
            while not found and stack:
                root = stack.pop()
                for ele in tree[root].keys():
                    # print(root, ele, prev)
                    if ele == prev:
                        max_edge = max(max_edge, tree[root][ele])
                        continue
                    if ele == destination:
                        max_edge = max(max_edge, tree[root][ele])
                        return max_edge
                    found, edge = get_max_edge_in_subtree(ele, destination)
                    if found:
                        max_edge = max(max_edge, edge)
                        cache[(source, destination)] = max_edge
                        return max_edge
                prev = root
            return max_edge
        # print(tree)
        ans = []
        for ele in B:
            stack = [1]
            get_path(1, ele[0], stack)
            print(ele)
            max_edge, found = get_max_edge_in_subtree(ele[0], ele[1])
            print("Before", max_edge, found, ele, stack)
            if not found:
                max_edge = get_max_edge_in_stack(ele[0], ele[1], stack)
            print("After", max_edge, found, ele, stack)
            ans.append(max_edge)
        return ans

            

print(Solution().solve([[6, 2, 19896], [10, 5, 5448], [5, 2, 21727], [8, 2, 14772], [2, 1, 11539], [3, 1, 1870], [9, 8, 19913], [7, 6, 25668], [4, 1, 26300]]
,[[8, 1], [7, 4], [9, 3], [8, 1], [10, 8], [7, 4], [8, 1], [10, 5]]))

    # {
    #     1: (2, 11), (3, 1), (6, 200)
    #     2: (4,12), (5, 100)
    #     6: (5, 20)
    # }