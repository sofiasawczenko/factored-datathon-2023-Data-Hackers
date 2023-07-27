!pip install azure-storage-file-datalake --pre

Con esto listo los nombres:

from azure.storage.filedatalake import FileSystemClient

file_system = FileSystemClient.from_connection_string("BlobEndpoint=https://safactoreddatathon.blob.core.windows.net;SharedAccessSignature=sp=rle&st=2023-07-25T18:12:36Z&se=2023-08-13T02:12:36Z&sv=2022-11-02&sr=c&sig=l2TCTwPWN8LSM922lR%2Fw78mZWQK2ErEOQDUaCJosIaw%3D;", 
                                                      file_system_name="source-files")    
paths = file_system.get_paths()
for path in paths:
    print(path.name + '\n')

Con esto bajo los archivos:

from azure.storage.filedatalake import DataLakeDirectoryClient

def download_file_from_directory(directory_client: DataLakeDirectoryClient, local_path: str, file_name: str):
    file_client = directory_client.get_file_client(file_name)

    with open(file=os.path.join(local_path, file_name), mode="wb+") as local_file:
        download = file_client.download_file()
        local_file.write(download.readall())
        local_file.close()
directory_clients=DataLakeDirectoryClient("https://safactoreddatathon.blob.core.windows.net;SharedAccessSignature=sp=rle&st=2023-07-25T18:12:36Z&se=2023-08-13T02:12:36Z&sv=2022-11-02&sr=c&sig=l2TCTwPWN8LSM922lR%2Fw78mZWQK2ErEOQDUaCJosIaw%3D;",directory_name="amazon_metadata",file_system_name="source-files")

download_file_from_directory(directory_client=directory_clients,file_name="amazon_metadata/name", local_path="local_directory")
