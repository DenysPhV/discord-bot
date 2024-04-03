import requests


def get_numbers(api_key, async_inbox=True, limit=100, slot=None):
    url = "https://api.textchest.com/numbers"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"async_inbox": async_inbox, "limit": limit, "slot": slot}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get numbers. Status code: {response.status_code}")
        return None
