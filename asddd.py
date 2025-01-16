import requests

def fetch_raydium_v3_data_paginated(
    mint1="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    mint2="So11111111111111111111111111111111111111112",
    pool_type="all",
    pool_sort_field="default",
    sort_type="desc",
    page_size=1000,  # page_size 최대값을 1000으로 가정
):
    """
    Raydium v3 API를 여러 페이지에 걸쳐 조회하는 함수 예시
    (page_size 최대 1000으로 설정)

    API 응답 예시 구조:
    {
      "id": "...",
      "success": true,
      "data": {
        "count": <int>,          # 현재 페이지에 대한 아이템 개수
        "data": [...],           # 실제 풀 정보들
        "hasNextPage": <bool>    # 다음 페이지 존재 여부
      }
    }
    """
    
    base_url = "https://api-v3.raydium.io/pools/info/mint"
    all_items = []

    page = 1
    while True:
        params = {
            "mint1": mint1,
            "mint2": mint2,
            "poolType": pool_type,
            "poolSortField": pool_sort_field,
            "sortType": sort_type,
            "pageSize": page_size,
            "page": page
        }

        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[Error] Request failed on page {page}: {e}")
            break  # 네트워크/HTTP 오류 발생 시 중단 (상황에 따라 재시도 로직 추가 가능)

        result_json = response.json()

        # success 필드 검사
        success = result_json.get("success", False)
        if not success:
            print(f"[Error] 'success' == false on page {page}")
            break

        body_data = result_json.get("data", {})
        items = body_data.get("data", [])
        all_items.extend(items)

        has_next_page = body_data.get("hasNextPage", False)

        if not has_next_page:
            # 다음 페이지가 없으면 반복 종료
            break

        page += 1

    return all_items

def print_data(data):
    # 응답 데이터를 원하는 대로 출력
    for i, item in enumerate(data):
        item_type = item.get("type", "")
        item_lp_address = item.get("id", "")
        print(f"{i} pool type: {item_type}, LP address: {item_lp_address}")

if __name__ == "__main__":
    # A, B 토큰 주소 예시는 USDT, USDC
    mints = ['Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB', 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v']
    results = fetch_raydium_v3_data_paginated(mint1=mints[0], mint2=mints[1])
    print_data(results)
