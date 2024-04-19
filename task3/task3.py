import json

with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)

with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

testss = tests_data['tests']
for test_item in testss:
    test_id = test_item['id']
    for value_item in values_data['values']:
        if value_item['id'] == test_id:
            test_item['value'] = value_item['value']
            break



with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)
print("Результат записан в файл report.json")