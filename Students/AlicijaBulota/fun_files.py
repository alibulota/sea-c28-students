import codecs


def funct(file_name):
    """remove all leading and trailing white spaces"""
    file_read = codecs.open(file_name, 'r')
    file_lines = file_read.readlines()
    rem_lines = map(str.strip, file_lines)
    file_read.close()

    while True:
        write_out = raw_input("New file (c) or overwrite existing file (o): ")
        if write_out.lower() == 'o':
            break
        elif write_out.lower() == 'c':
            file_name = raw_input("New file name: ")
            break

    write_file = codecs.open(file_name, 'w')

    for line in rem_lines:
        write_file.write(line + '\n')
    print '"{}" has no leading or trailing white spaces.'.format(file_name)
