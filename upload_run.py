import dropbox
import os

dbx = dropbox.Dropbox('bF6SpHPebAgAAAAAAABGfQBin3OqrxpM0EdiXFE-C5GRJwrLy9Nh12135DHwXmKFtg1')
dbx.users_get_current_account()

# Fichero
file = "26_11_2017_14_03_00_CNP.zip"

tamano_maximo_megas = 50
CHUNK_SIZE = tamano_maximo_megas * 1024 * 1024
file_size = os.path.getsize(file)

print CHUNK_SIZE
print file_size

if file_size <= CHUNK_SIZE:
    # Upload
    f = open(file, 'rb')
    response = dbx.files_upload( f.read(), '/' + file)
    print 'uploaded: ', response

    # Imprimimos la fecha de subida
    dropbox_fecha_subida = dbx.files_get_metadata('/'+file).server_modified
    print dropbox_fecha_subida
