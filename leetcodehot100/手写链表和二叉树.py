class ListNode:
    def __init__(self,val,next_=None):
        self.val =val
        self.next = next_
def build_listnode(arr):
    dummy = ListNode(0)
    cur =  dummy
    for x in arr:
        cur.next = ListNode(x)
        cur =cur.next
    return dummy.next

# 记忆要点： 虚拟头节点，循环更新，初始化不要忘记设置None

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val =val 
        self.left =left
        self.right =right
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    root =  TreeNode(arr[0])
    q =deque([root])
    i =1
    while q and i < len(arr):
        node = q.popleft()
        for side in ("left","right"):
            if i < len(arr) and arr[i] is not None:
                child =   TreeNode(arr[i]) 
                setattr(node,side,child)
                q.append(child)
            i+=1
    return root
# 记忆要点： 用到setattr,队列更新！i从1开始


