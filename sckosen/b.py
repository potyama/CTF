def caesar(data,num):
    ans = []
    for i in range(len(data)):
        temp = ord(data[i])
        if 97 <= temp <= 122: #ASCII CODE 97が"a", 122が"z"
            if temp - num < 97:#aの次はzとしている
                ans.append(chr(123-(97-(temp-num))))
            else:    
                ans.append(chr(temp-num))
        elif 65 <= temp <= 90:#ASCII CODE 65が"A",90が"Z"        
            if temp -num < 65:#Aの次はZとしている
                ans.append(chr(91-(65-(temp-num))))
            else:
                ans.append(chr(temp-num))
        else:
            ans.append(chr(temp))
    temp_ans = "".join(ans)
    if "is" in temp_ans or "am" in temp_ans or "are" in temp_ans :
        judge = True
    else:
        judge = False
    return temp_ans,judge
    # print("".join(ans))
 
if __name__ == "__main__":
    data = input("復号化する文字列\n")
    pos_ans =[] #答えとしての有力候補
    npos_ans =[]
 
    pos_index = []#何文字ずらしたか格納
    npos_index = []
 
    for i in range(1,26):
        temp_ans,judge = caesar(data, i)
        if judge:
            pos_ans.append(temp_ans)
            pos_index.append(i)
        else:
            npos_ans.append(temp_ans)
            npos_index.append(i)
 
    if len(pos_ans) != 0:
        print("\n有力候補")
        for i in range(len(pos_ans)):
            print("{}文字ずらした場合\n {}".format(pos_index[i],pos_ans[i]))
        print("\nその他")
        for i in range(len(npos_ans)):
            print("{}文字ずらした場合\n {}".format(npos_index[i],npos_ans[i]))
    else:
        print("有力候補は見つかりませんでした。")
        for i in range(len(npos_ans)):
            print("{}文字ずらした場合\n {}".format(npos_index[i],npos_ans[i]))
