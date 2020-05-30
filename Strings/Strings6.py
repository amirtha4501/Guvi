st = str(input())
num = []
for word in st.split():
  word = word.replace('.', '')
  if word.isdigit():
    num.append(int(word))
max = num[0]
for i in range(len(num)):
  if num[i] > max:
    max = num[i]
print(max)