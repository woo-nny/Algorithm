H,M = input().split()
H = int(H)
M = int(M)
M_sum = (H*60+M)-45
H_answer=M_sum//60
M_answer=M_sum%60
if H_answer < 0 :
    H_answer +=24
print(H_answer,M_answer)
