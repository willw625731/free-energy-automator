
def top_dict(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    sections = file.split('\n\n')

    cut_points = ('[ atomtypes ]', '[ moleculetype ]', '[ system ]', '[ molecules ]')

    key_idx = []
    for n, block in enumerate(sections):
        for key_word in cut_points:
            if key_word in block:
                key_idx.append(n)

    file_dict = {'preamble':'\n\n'.join(sections[0:key_idx[0]]).split('\n'),
                 'atomtypes':'\n\n'.join(sections[key_idx[0]:key_idx[1]]).split('\n'),
                 'parameters':'\n\n'.join(sections[key_idx[1]:key_idx[2]]).split('\n'),
                 'system':'\n\n'.join(sections[key_idx[2]:key_idx[3]]).split('\n'),
                 'molecules':'\n\n'.join(sections[key_idx[3]:]).split('\n')}

    
    return file_dict

def add_top(top1_dict, top2_dict, name='molecule', count=1):
    comb_dict = top1_dict
    atoms = [top1_dict['atomtypes'][2:][n].split()[0] for n in range(len(top1_dict['atomtypes'][2:]))]
    for n, atom_type in enumerate(top2_dict['atomtypes'][2:]):
        new_atom = top2_dict['atomtypes'][2:][n].split()[0]
        if new_atom not in atoms:
            top1_dict['atomtypes'].append(atom_type)      
    
    comb_dict['parameters'] += ['\n']
    comb_dict['parameters'] += top2_dict['parameters']
        
    if comb_dict['molecules'][-1] == '':
        comb_dict['molecules'].pop()
        comb_dict['molecules'] += [name + '\t\t' + str(count)]
        comb_dict['molecules'] += ''
    else:
        comb_dict['molecules'] += [name + '\t\t' + str(count)]
    return comb_dict

def dict_top(comb_dict):
    for key in comb_dict:
        comb_dict[key] = '\n'.join(comb_dict[key])
    sections = []
    for key in comb_dict:
        sections.append(comb_dict[key])
    return '\n\n'.join(sections)

def write_str(final, file_name):
    with open(file_name, 'w') as f:
        f.write(final)
        
def top_comp(file1, file2, mol2, count, file_out):
    write_str(dict_top(add_top(top_dict(file1), top_dict(file2), mol2, count)), file_out)
       
        
        
def comb_coords(file1, file2, file_out):
    with open(file1, 'r') as f:
        file1 = f.read()
    lines1 = file1.split('\n')
    if lines1[-1] == '':
        lines1.pop()
        
    with open(file2, 'r') as f:
        file2 = f.read()
    lines2 = file2.split('\n')
    if lines2[-1] == '':
        lines2.pop()
        
    lines2.pop(0)
    lines2.pop(0)
    lines2.pop()
    
    for line in lines2:
        lines1.insert(-1, line)
    lines1[1] = str(len(lines1) - 3)
    final = '\n'.join(lines1)
    
    with open(file_out, 'w') as f:
        f.write(final)

