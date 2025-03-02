def get_first_quotation_idx(line):
    return line.index('"')

def get_second_quotation_idx(line, l_idx):
    return line[l_idx+1:].index('"') + l_idx + 1

def determineRightSplit(line, l_idx):
    second_quotation = get_second_quotation_idx(line, l_idx)
    lst_idx = len(line) - 1
    if second_quotation == lst_idx:
        return None
    if second_quotation + 1 == lst_idx:
        return ''
    else:
        return line[second_quotation + 2:]

def recursive_split(line):
    if line is None:
        return []
    if '"' not in line:
        return line.strip().split(',')
    l_idx = get_first_quotation_idx(line)
    line_properties = []
    left_properties = []
    if line[0] != '"':
        left_properties.extend(line[0: line.index(',"')].strip().split(','))
    line_properties.extend(left_properties)
    line_properties.append(line[l_idx+1: get_second_quotation_idx(line, l_idx)])
    right_properties = recursive_split(
        determineRightSplit(line, l_idx)
    )
    line_properties.extend(right_properties)
    return line_properties