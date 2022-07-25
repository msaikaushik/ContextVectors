# text_file = open('global.txt', 'r')
# text = text_file.read()


# #finding unique
# unique = []
# for word in text:
#     if word not in unique:
#         unique.append(word)

import json

with open('pan20-authorship-verification-training-small.jsonl', 'r') as json_file:
    json_list = list(json_file)

# for json_str in json_list:
#     result = json.loads(json_str)
#     print(f"result: {result}")
#     print(isinstance(result, dict))

js = json_list[0]
result = json.loads(js)
# tx = js["pair"][0]
k = result['pair']
print(k[0])