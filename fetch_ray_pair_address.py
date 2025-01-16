from web3 import Web3

# Web3 인스턴스 생성
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/29ac4a6abab2469cb0d87fa1fedef4d6'))

# 프록시 관리자 슬롯 정의
proxy_admin_slot = "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"  # 구현 슬롯

# 실제 주소로 mock_bridge_address 정의
mock_bridge_address = "0x39954De76b4F64E7eA5D7f906fCD943dcEF6f9Bb"

# 슬롯에서 주소 읽기
implementation_address = web3.eth.get_storage_at(mock_bridge_address, proxy_admin_slot).hex()  # 슬롯에서 주소 읽기

# 40자리 주소 추출
implementation_address = Web3.to_checksum_address(f"0x{implementation_address[-40:]}")  # 40자리 주소 추출

# 구현 주소 출력
print(f"Implementation Address: {implementation_address}")