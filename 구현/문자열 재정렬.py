data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)
    
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 리스트를 문자열로 변환
print(''.join(result))

# --------------------------------------------------------
# 내 풀이
data = input()
alphabet = []
number = 0
number_count = 0

for i in data:
    if i.isalpha():
        alphabet.append(i)
    else:
        number += int(i)
        number_count += 1

alphabet.sort()

if number_count == 0:
    print(''.join(alphabet))
else:
    print(''.join(alphabet) + str(number))
