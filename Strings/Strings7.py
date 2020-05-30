# delete all the repeating characters
import collections

s = str(input())
st_dic = collections.Counter(s)
st = []

for char in st_dic:
  if st_dic[char] == 1:
    st.append(char)

print(*st, sep='')