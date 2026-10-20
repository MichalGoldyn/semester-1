# semester-1
Week by week content for semester of COMP1850: lecture notes, in-class tasks, worksheets





plist2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
          'ccg', 'cca', 'ata']
charset2 = ['a', 'c', 't', 'g']
print(valid_char_in_string(plist2, charset2))  # True

plist3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
charset3 = ['a', 'c']
print(valid_char_in_string(plist3, charset3))  # False

plist4 = ['00000', '00001', '00010', '00011', '00100']
charset4 = '01'
print(valid_char_in_string(plist4, charset4))  # False