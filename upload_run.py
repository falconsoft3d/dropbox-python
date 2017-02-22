import dropbox

client = dropbox.client.DropboxClient('1bF6SpHPebAgAAAAAAABDuS1GCQ8QBXEgvxBDj4X1EdwLLVlTiE54wdcoLP1dtjaQ')
print 'linked account: ', client.account_info()

f = open('2.zip', 'rb')
response = client.put_file('/magnum-opus.zip', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.zip', 'wb')
out.write(f.read())
out.close()
print metadata