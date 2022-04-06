

from numpy import isin


def recursive(lst, ans):
    for i in lst:
        if isinstance(i, list):
            print(i)
            recursive(i, ans)
        else:
            ans.append(i)
def flatten(lst):
    ans = []

    rec = lambda x: ans.append(x) if not isinstance(x, list) else rec(x)

    # recursive(lst, ans)
    return ans






print(flatten([1,2,3,[4,5,[6,7,8, [9, 10]], 11, 12, [14, 15]]]))