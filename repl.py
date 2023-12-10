import json

data = open('data/gl-dependency-scanning-report.json','r')
data_json = json.loads(data.read())
vuln = data_json['vulnerabilities']
description = data_json['description']
severity = data_json['severity']
scanner = data_json['scanner']['name']
namespace = data_json['namespace']
identifiers = data_json['identifiers']

print("Description:", description)
print("Severity:", severity)
print("Scanner:", scanner)
print("Namespace:", namespace)
print("Identifiers:")
for identifier in identifiers:
    print("  Type:", identifier['type'])
    print("  Name:", identifier['name'])
    print("  Value:", identifier['value'])
    print("  URL:", identifier['url'])
    print()