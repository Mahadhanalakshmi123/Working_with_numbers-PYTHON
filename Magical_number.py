def count_magical_numbers(N):
    magical_count = 0
    
    for num in range(1, N + 1):
        binary_str = bin(num)[2:].replace('1', '2').replace('0', '1')
        digit_sum = sum(int(digit) for digit in binary_str)
        
        if digit_sum % 2 != 0:
            magical_count += 1
    
    return magical_count

input1 = 2
result = count_magical_numbers(input1)
print(result) 
