data_long = ["flower","flow","flight"]


# for datas in data_long:
#     for data in range(len(datas)):
#         print(datas[data] )
#     print(datas)



for datas in data_long:
    for data in [x for x in data_long if x != datas]:
        pass
    print()



