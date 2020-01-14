import zipfile
import os
#! backup folderow z plikami coby nic nie ucieklo

def backup_to_zip(folder):

    folder = os.path.abspath(folder) # pobieramy absolutna sciezke przez abspath

    # sprawdzam, czy backup juz powstal i jezeli tak, to kolejny backup bedzie mial next number
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    # TODO create zip file
    print('Creating %s...' % zip_filename)
    new_zip = zipfile.ZipFile(zip_filename, 'w')

    # TODO walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        new_zip.write(foldername)
        for filename in filenames:
            new_ = os.path.basename(folder) + '_'
            if filename.endswith(new_) and filename.endswith('.zip'):
                continue
            new_zip.write(os.path.join(foldername, filename))
    new_zip.close()
    print('done')


backup_to_zip('C:\\Users\\pisko\\OneDrive\\Pulpit\\python scripts')