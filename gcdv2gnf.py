import os
header = 'GNF'.encode()
folder = 'E:\GRR\gcd\\'
output_folder = 'E:\GRR\gnf\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(folder):
    for file in f:
        if '.gcdm' in file:
            pass
        elif '.gcdv' in file:
            files.append(os.path.join(r, file))
        elif '.gcd' in file:
            files.append(os.path.join(r, file))


for file_path in files:
    with open(r'%s' % (file_path), 'rb') as f:
        print("Open File: %s" % (f.name))
        data = f.read()
        count = 0
        header_index = data.find(header, 0)
        next_header_index = data.find(header, header_index + len(header))

        if header_index >= 0 and next_header_index >= 0:

            print("Found header at %s and ending at %s" \

                  % (header_index, next_header_index))
            body = data[header_index: next_header_index]

            while body is not None:
                with open(r"%s%s_%d.gnf" % (output_folder, os.path.basename(f.name).split('.')[0], count), "wb") as output:
                    output.write(body)
                    print("Exported #%d" % count)
                    count += 1

                header_index = next_header_index
                next_header_index = data.find(header,\
                                         next_header_index + len(header) )

                if header_index >= 0 and next_header_index >= header_index:
                    print("Found header at %s and ending at %s" \
                           % (header_index, next_header_index))
                    body = data[header_index: next_header_index]
                else:
                    print("Found header at %s and ending at %s" \
                          % (header_index, len(data)))
                    body = data[header_index: len(data)]
                    #print("body: %s" % body)
                    with open(r"%s%s_%d.gnf" % (output_folder, os.path.basename(f.name).split('.')[0], count), "wb") as output:
                        output.write(body)
                        print("Exported #%d" % count)
                        count += 1
                    break
    print("Export completed with %d gnfs exported" % (count))
