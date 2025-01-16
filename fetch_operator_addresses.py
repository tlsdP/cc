from web3 import Web3

# Infura 프로젝트 ID를 사용하여 Web3 인스턴스 생성
infura_project_id = '29ac4a6abab2469cb0d87fa1fedef4d6'
infura_url = f'https://mainnet.infura.io/v3/{infura_project_id}'
web3 = Web3(Web3.HTTPProvider(infura_url))

# 계약 주소 및 ABI 설정
contract_address = '0x39954De76b4F64E7eA5D7f906fCD943dcEF6f9Bb'
contract_abi = [
    {"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"address","name":"initialOwner","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"},
    {"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},
    {"inputs":[{"internalType":"address","name":"admin","type":"address"}],"name":"ERC1967InvalidAdmin","type":"error"},
    {"inputs":[{"internalType":"address","name":"implementation","type":"address"}],"name":"ERC1967InvalidImplementation","type":"error"},
    {"inputs":[],"name":"ERC1967NonPayable","type":"error"},
    {"inputs":[],"name":"FailedInnerCall","type":"error"},
    {"inputs":[],"name":"ProxyDeniedAdminAccess","type":"error"},
    {"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":False,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},
    {"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},
    {"stateMutability":"payable","type":"fallback"}
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def get_operator_addresses():
    operator_count = contract.functions.getOperatorCount().call()
    operators = []

    for i in range(operator_count):
        operator = contract.functions.getOperator(i).call()
        if operator['weight'] > 0:
            operators.append(operator['address'])

    operators.sort()
    print(f"SCAN2024{{{', '.join(operators)}}}")

get_operator_addresses()

