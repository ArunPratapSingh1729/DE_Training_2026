input = "cbbd"

longest_substring = ''
longest_substring_length = 0

for i in range(len(input)):

    left = i - 1
    right = i + 1
    while left >= 0 and right < len(input):
        if input[left] == input[right]:
            substring_length = (right - left) + 1
            if substring_length > longest_substring_length:
                longest_substring_length = substring_length
                longest_substring = input[left:right+1]
        else:
            break
        left -= 1
        right += 1

    left = i
    right = i + 1
    while left >= 0 and right < len(input):
        if input[left] == input[right]:
            substring_length = (right - left) + 1
            if substring_length > longest_substring_length:
                longest_substring_length = substring_length
                longest_substring = input[left:right+1]
        else:
            break
        left -= 1
        right += 1

print("The longest substring is : ", longest_substring)

