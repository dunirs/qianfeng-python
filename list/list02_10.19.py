# 提示输入一个单词 比如 hello 如果输入的单词在列表中，则删除

words = ['hello', 'good', 'agoo', 'helgo', 'go', 'digit', 'alpha' ]
w = input('请输入一个单词：')
"""
# 方式1
# 方式1存在一些问题，当 words = ['hello', 'good', 'agoo', 'helgo', 'digit', 'alpha']
# 我输入 go 应该删除 good agoo helgo 但是结果删除干净
# 原因是在删除时 列表就发生变化了 而下标i却在持续增长
l= len(words)
i = 0
while i < l:
    if w in words[i]:
        del words[i]
        l -= 1
        i -= 1  # 解决存在的问题 在列表删除一个元素时 下标也减一 或者写 continue：就是不执行 i += 1 这条语句 而直接跳到while循环处执行下一条循环
    i +=1

print(words)
"""


# 方式2
# 方式2也存在上述问题，
# 解决这个问题的方法：从后往前删
for word in words[::-1]:
    if w in word:
        del words[words.index(word)]
print(words)




