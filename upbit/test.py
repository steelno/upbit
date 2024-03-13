import pyupbit
access = "xXX7OxneP2ysfxH9vxsvb96ZvRN7wJ3OxJECid4q"          # 본인 값으로 변경
secret = "zFMjcgklyALLfXWhx8lotnzW9Z0Bgonz3lQKbLcq"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회