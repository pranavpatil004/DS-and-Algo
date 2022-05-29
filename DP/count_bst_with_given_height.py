MOD= 1000000007
choose=[]
dp=[]
def add(x,y):
    x += y
    x%=MOD

def build(N):
    global choose
    choose[0][0]=1
    for i in range(1,2*N+1):
        choose[i][0]=1
        for j in range(1,i+1):
            choose[i][j]=choose[i-1][j]
            choose[i][j]+=choose[i-1][j-1]
            choose[i][j]%=MOD

def rec(n,h):
    global choose 
    global dp
    if(n<=1):
        return(h==0)
    if(h<0):
        return 0
    if(dp[n][h]!=-1):
        return dp[n][h]
    ret=0
    x=0
    y=0
    for i in range(1,n+1):
        x=i-1
        y=n-x-1
        sum1=0
        sum2=0
        ret1=0
        for j in range(h-1):
            sum1+=rec(x,j)
            sum1%=MOD
            sum2+=rec(y,j)
            sum2%=MOD
        ret1+=sum1*rec(y,h-1)
        ret1+=sum2*rec(x,h-1)
        ret1+=rec(x,h-1)*rec(y,h-1)
        ret1=ret1*choose[x+y][y]
        ret+=ret1
        ret%=MOD
    dp[n][h]=ret    
    return ret
    
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        n=A
        global choose
        global dp
        choose=[]
        dp=[]
        dp=[[-1]*(n+1) for i in range(n+1)]
        choose=[[0]*(2*n+1) for i in range(2*n+1)]
        build(n)
        return int(rec(A,B))

Solution().cntPermBST(4, 2)