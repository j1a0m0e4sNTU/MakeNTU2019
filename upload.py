import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess


def upload(path,filename,blobname):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='andymakentu', account_key='uCnL324uEg858PVX2NXgqBQ+hfTht8P3/x5m5qzZeZPvLn/it+pnOhdZfZmJp7sGH+vhZYJdoeFmyQ7o8CZstA==pip install azure-storage-blob')

        # Create a container called 'quickstartblobs'.
        container_name ='pictureblobs'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Create a file in Documents to test the upload and download.
        local_path=os.path.expanduser(path)
        local_file_name =filename
        full_path_to_file =os.path.join(local_path, local_file_name)


        print("\nUploading to Blob storage as blob:" + local_file_name)

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, blobname, full_path_to_file)

    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    upload('~/Desktop/wutj','myp.jpeg','haha.jpeg')



