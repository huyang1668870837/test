# #最长公共子串
# ###
# def find_Substring(str_1,str_2):
#     num=[[0 for i in range(len(str_2)+1)]for j in range(len(str_1)+1)]
#     num_max=0   #子串的长度
#     str_end=0   #最长公共子串在str_1中的最后一位
#     for i in range(len(str_1)):
#         for j in range(len(str_2)):
#            if str_1[i]==str_2[j]:
#                num[i+1][j+1]=num[i][j]+1
#                if num[i+1][j+1]>num_max:
#                    num_max=num[i+1][j+1]
#                    str_end=i+1
#     return str_1[str_end-num_max:str_end],num_max
#
# print(find_Substring("str_1","str_2"))


#最长公共子序列
def find_Subsequence(str_1,str_2):
    num = [[0 for i in range(len(str_2) + 1)] for j in range(len(str_1) + 1)]
    flag= [[0 for i in range(len(str_2)+1)]for j in range(len(str_1)+1)]
    for i in range(len(str_1)):
        for j in range(len(str_2)):
            if str_1[i]==str_2[j]:
                num[i+1][j+1]=num[i][j]+1
                flag[i+1][j+1]="ok"
            elif num[i][j+1]>=num[i+1][j]:
                num[i+1][j+1]=num[i+1][j]
                flag[i+1][j+1]="up"
            else:
                num[i+1][j+1]=num[i+1][j]
                flag[i+1][j+1]="left"
    return num,flag
#递归
def fun(flag,str_1,i,j):
    if i==0 or j==0:
        return
    if flag[i][j]=="ok":
        print(str_1[i-1],end="")
        fun(flag,str_1,i-1,j-1)
    elif flag[i][j]=="left":
        fun(flag, str_1, i,j-1)
    else:
        fun(flag, str_1, i - 1, j)
#非递归：
def fun_1(flag,str_1,i,j):
    subseq=""
    while i!=0 or j!=0:
        if flag[i][j]=="ok":
            subseq+=str_1[i-1]
            i=i-1
            j=j-1
        elif flag[i][j]=="left":
            j=j-1
        else:
            i=i-1
    return subseq
str_1="ABCBDAB"
str_2="BDCABA"
num,flag=find_Subsequence(str_1,str_2)
fun(flag,str_1,len(str_1),len(str_2))
print(fun_1(flag,str_1,len(str_1),len(str_2)))