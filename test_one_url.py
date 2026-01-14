import requests

url = "https://www.pixelglobalit.com/about-us/"

print("Sending request...")
response = requests.get(url, timeout=20)

print("Status Code:", response.status_code)
print("Response length:", len(response.text))

print("\nRAW RESPONSE (first 500 chars):\n")
print(response.text[:500])
