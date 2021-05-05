import pyupbit

access = "zsyAV84HQo64D5YjQ8ilLKL7gZ8sJoWwwfWIalH2"          # 본인 값으로 변경
secret = "bxK8fNI8VWNL3ogakZWpZEQ2xSOn8FjEHO7HuNfd"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
