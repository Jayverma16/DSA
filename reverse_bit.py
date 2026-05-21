def reverseBits(n: int) -> int:
    rev = 0
    for _ in range(32):
        rev <<= 1          # Shift result left
        rev |= (n & 1)     # Add last bit of n
        n >>= 1            # Shift n right
    return rev

if __name__ =="__main__":
    answer =  reverseBits(25)
    print(answer)