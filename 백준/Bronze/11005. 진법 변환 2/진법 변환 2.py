n,p = input().split()
n,p = int(n),int(p)
def to_base36(n):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n > 0:
        n, remainder = divmod(n, p)
        result = chars[remainder] + result
    return result


print(to_base36(n))
