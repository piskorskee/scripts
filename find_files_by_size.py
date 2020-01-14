import os, send2trash


def selective_copy(folder):

    for foldername, subfolders, filenames in os.walk(folder):
        x1 = os.path.join(folder, foldername)
        for filename in filenames:
            x2 = os.path.join(x1, filename)
            x = os.path.getsize(x2)
            if x > 111111:
                print(os.path.abspath(filename))
                print('%s jest wiekszy' % (filename))



selective_copy('C:\\Users\\pisko\\OneDrive\\Pulpit')
