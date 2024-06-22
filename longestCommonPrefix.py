data_long = ["flower","flow","flight"]


# for datas in data_long:
#     for data in range(len(datas)):
#         print(datas[data] )
#     print(datas)




def longestCommonPrefix():
    res = ""
    for i in range(len(data_long[0])):
        for s in data_long:
            if i == len(s) or s[i] != data_long[0][i]:
                return(res)
        res += data_long[0][i]
    return(res)
        

print(longestCommonPrefix())