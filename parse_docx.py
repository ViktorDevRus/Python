from docx_parser import DocumentParser
import json


def table_processor(raw_table_dict):
    """Function for table data processing"""
    try:
        result = dict(raw_table_dict['data'])
        del result
        raw_list = raw_table_dict['data']
        level = 0
        j = 0
        parent_index = 0
        while j < len(raw_list):
            if raw_list[j][0] == raw_list[j][1]:
                raw_list[j][1] = {}
                level = 1
                parent_index = j
            elif (raw_list[j][0] != raw_list[j][1]) and (level == 1):
                raw_list[parent_index][1][raw_list[j][0]] = raw_list[j][1]
                del raw_list[j]
                continue
            j += 1
        return dict(raw_list)

    except ValueError as error:
        if raw_table_dict.get('merged_cells'):
            del raw_table_dict['merged_cells']
        j = 0
        while j < len(raw_table_dict['data']):
            raw_table_dict['data'][j] = list(dict.fromkeys(raw_table_dict['data'][j]))
            j += 1
        # print("Custom table: ", raw_table_dict, "\n")
        raw_list = raw_table_dict['data']
        if raw_list[0] == ['Param', 'Value', 'Source']:
            if len(raw_list[1]) == 1:
                del raw_list[0]
            level = 0
            j = 0
            parent_index = 0
            while j < len(raw_list):
                if (len(raw_list[j]) != 1) and (len(raw_list[j]) == 3) and (level == 0):
                    del raw_list[j][2]
                elif len(raw_list[j]) > 3:  # elif (len(raw_list[j]) != 1) and (len(raw_list[j]) != 3):
                    del raw_list[j]
                    continue
                elif len(raw_list[j]) == 1:
                    raw_list[j].append(dict())
                    level = 1
                    parent_index = j
                elif (len(raw_list[j]) != 1) and (len(raw_list[j]) in {2, 3}) and (level == 1):
                    if (len(raw_list[j]) == 2) and (j != len(raw_list) - 1) and (len(raw_list[j + 1]) > 3):
                        del raw_list[j]
                        continue
                    raw_list[parent_index][1][raw_list[j][0]] = raw_list[j][1]
                    del raw_list[j]
                    continue
                j += 1
            # print(raw_list, '\n\n')
            return dict(raw_list)

        elif raw_list[0] != ['Param', 'Value', 'Source']:
            if raw_table_dict.get('merged_cells'):
                del raw_table_dict['merged_cells']
            if raw_list[0] == ['License data']:
                level = 0
                j = 0
                parent_index = 0
                while j < len(raw_list):
                    if len(raw_list[j]) == 1:
                        raw_list[j].append(dict())
                        level = 1
                        parent_index = j
                    elif (len(raw_list[j]) == 2) and (level == 1):
                        raw_list[parent_index][1][raw_list[j][0]] = raw_list[j][1]
                        del raw_list[j]
                        continue
                    elif len(raw_list[j]) >= 3:
                        del raw_list[j]
                        continue
                    j += 1
                return dict(raw_list)
            # print("Custom table: ", raw_table_dict)
            # print(raw_list, '\n\n')
            return {'Default param': 'Value'}


# infile = 'tests/example_secretnet.docx'
infile = r'tests\converted-to-docx\secretnet.docx'
doc = DocumentParser(infile)
doc_list = list(doc.parse())
if not (doc_list is None):
    del doc

# Calculate start data indexes for host
arms_start_indexes = []
i = 0
while i < len(doc_list):
    if doc_list[i][0] == 'paragraph':
        if doc_list[i][1]['text'] == 'Ресурсы АРМ':
            arms_start_indexes.append(i)
    i += 1

# Form tuple of data indexes, belonging to each host
arms_data_indexes_pairs = []
i = 0
while i < len(arms_start_indexes):
    if i == (len(arms_start_indexes) - 1):
        arms_data_indexes_pairs.append((arms_start_indexes[i], len(doc_list)))
    else:
        arms_data_indexes_pairs.append((arms_start_indexes[i], arms_start_indexes[i + 1]))
    i += 1
arms_data_indexes_pairs = tuple(arms_data_indexes_pairs)

# Get data for each host
all_arms_data = []
for arms_data_indexes_pair in arms_data_indexes_pairs:
    arm_data = doc_list[arms_data_indexes_pair[0]:arms_data_indexes_pair[1]]
    arm_data_dict = {}
    i = 0
    level = 0
    last_item_type = ''
    parent_item_key = ''
    while i < len(arm_data):
        if arm_data[i][0] == 'paragraph' and level == 0 and (last_item_type == '' or last_item_type == 'table'):
            last_item_type = 'paragraph'
            arm_data_dict[arm_data[i][1]['text']] = {}

        elif arm_data[i][0] == 'multipart':
            del arm_data[i]
            continue

        elif arm_data[i][0] == 'table' and level == 0 and last_item_type == 'paragraph':
            last_item_type = 'table'
            arm_data_dict[arm_data[i - 1][1]['text']] = table_processor(arm_data[i][1])
            help = 0

        elif arm_data[i][0] == 'paragraph' and level == 0 and last_item_type == 'paragraph':
            last_item_type = 'paragraph'
            level += 1
            parent_item_index = i
            parent_item_key = arm_data[i - 1][1]['text']
            arm_data_dict[parent_item_key][arm_data[i][1]['text']] = {}

        elif arm_data[i][0] == 'table' and level == 1 and last_item_type == 'paragraph':
            last_item_type = 'table'
            arm_data_dict[parent_item_key][arm_data[i - 1][1]['text']] = table_processor(
                arm_data[i][1])

        elif arm_data[i][0] == 'paragraph' and level == 1 and last_item_type == 'table':
            last_item_type = 'paragraph'
            if i != len(arm_data) - 1:
                if arm_data[i + 1][0] == 'paragraph':
                    level -= 1
                    parent_item_key = arm_data[i][1]['text']
                    arm_data_dict[arm_data[i][1]['text']] = {}
                elif arm_data[i + 1][0] == 'table':
                    arm_data_dict[parent_item_key][arm_data[i][1]['text']] = {}
            else:
                arm_data_dict[arm_data[i][1]['text']] = {}
                break
        i += 1
    print(arm_data_dict)

    filename = f'{arm_data_dict["PC Resources"]["PC:"]}.json'
    with open(filename, 'w') as file_object:
        json.dump(arm_data_dict, file_object)
all_arms_data.append(arm_data_dict)

print('Parsing done.')
doc_list = None
