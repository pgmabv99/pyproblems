from typing import List
# Write any import statements here

# def util(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
#   # Write your code here
#   ns=0
#   nt=0
#   while True:
#     nsm=ns%C
#     for i in range(N):
#       if nsm>A[i] and nsm<=B[i]:
#         nt+=1
#         break
#     if nt == K:
#       break
#     ns+=1
#   return ns



def util(C: int, N: int, ax, K: int) -> int:
  # Write your code here
  ns=0
  totk=0


  # print(ax)
  for i in range(N):
    a=ax[i][0]
    b=ax[i][1]
    len1=b-a
    if totk + len1 < K:
      totk+=len1
    else:
      df=K-totk
      ns=a+df
      break
  return ns


def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  # Write your code here
  tun1=0
  for i in range(len(A)):
    tun1+=B[i]-A[i]

  n=K//tun1
  rmd=K%tun1

  ax=[]
  for i in range(N):
    ax.append((A[i],B[i]))
  ax.sort()

  # print("tun time for  one  full", tun1, "n", n, "rmd", rmd)
  if rmd > 0:
    ns1=n*C
    ns2=util(C,N,ax,rmd)
    ns=ns1+ns2
  else:
    ns1=(n-1)*C
    ns2=ax[N-1][1]
    ns=ns1+ns2
  return ns

# res=getSecondsElapsed(10,2,[1, 6],[3, 7],7)
# print(res)
# res=getSecondsElapsed(50,3,[39, 19, 28],[49, 27, 35],15)
# print(res)
res=getSecondsElapsed(6,2,[1, 3],[2,4],3)
print(res)