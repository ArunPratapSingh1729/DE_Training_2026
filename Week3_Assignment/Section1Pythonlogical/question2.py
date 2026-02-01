s = "hello world" 
output = list({c for c in s if s.count(c) > 1 and c != " "})

print(output)