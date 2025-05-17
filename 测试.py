from werkzeug.security import generate_password_hash, check_password_hash


# 哈希函数的加解密验证
hash_password = generate_password_hash('123456')
print(hash_password)
print(len(hash_password))

hash_password = 'scrypt:32768:8:1$CuYlHniUlsQ9UVnm$f4182766015226d46b4151610c6081a67d1e6be2aed1f9cb81c392aa927a8237540502c0fc7dd1c9fd2f0c6a660e69ce81f2e6e4fac5192ae25ea1f8a37ac5fa'

result = check_password_hash(hash_password, '123456')
print(result)


