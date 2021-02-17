from collections import OrderedDict

vocabulary_list = OrderedDict()

vocabulary_list['if'] = 'condition expression'
vocabulary_list['while'] = 'loog expression'

for key, value in vocabulary_list.items():
    print("\nKey: " + key)
    print("Value: " + value)