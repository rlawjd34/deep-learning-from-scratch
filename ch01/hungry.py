print("I'm hungry!")
import requests

rj = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()

ips = [prefix['ip_prefix'] for prefix in rj['prefixes'] if prefix['service'] == 'EC2' and prefix['region'] == 'ap-northeast-2']

print(', '.join(ips))