s = "arun pratap singh"
character_arr = {}

for ch in s:
    character_arr[ch] = character_arr.get(ch , 0) + 1

print(character_arr)