from __future__ import annotations

import os
import tempfile

from gcs_crud import (
    upload_file,
    upload_bytes,
    download_file,
    download_bytes,
    list_objects,
    get_metadata,
    delete_object,
    copy_object,
    move_object,
)


def main() -> None:
    bucket_name = os.environ.get("GCS_BUCKET", "tungtran-bucket")
    project_id = os.environ.get("GCP_PROJECT_ID", "learn-cloud-473302")

    # Create a temp file to upload
    with tempfile.NamedTemporaryFile("w+b", delete=False) as tmp:
        tmp.write(b"Hello from GCS CRUD example!\n")
        tmp_path = tmp.name

    dest_blob = "examples/hello.txt"

    print("Uploading file...")
    uri = upload_file(bucket_name, dest_blob, tmp_path, project_id=project_id, content_type="text/plain")
    print("Uploaded to:", uri)

    print("Listing objects with prefix 'examples/'...")
    print(list_objects(bucket_name, prefix="examples/", project_id=project_id))

    print("Getting metadata...")
    print(get_metadata(bucket_name, dest_blob, project_id=project_id))

    print("Downloading to bytes...")
    data = download_bytes(bucket_name, dest_blob, project_id=project_id)
    print("Downloaded bytes:", data)

    # Copy and move
    print("Copying object...")
    copied_uri = copy_object(bucket_name, dest_blob, bucket_name, "examples/hello-copy.txt", project_id=project_id)
    print("Copied to:", copied_uri)

    print("Moving object...")
    moved_uri = move_object(bucket_name, "examples/hello-copy.txt", bucket_name, "examples/hello-moved.txt", project_id=project_id)
    print("Moved to:", moved_uri)

    # Download to a local path
    print("Downloading to local file...")
    local_download = os.path.join(tempfile.gettempdir(), "hello-downloaded.txt")
    print(download_file(bucket_name, dest_blob, local_download, project_id=project_id))

    # Clean up
    print("Deleting original object...")
    delete_object(bucket_name, dest_blob, project_id=project_id)
    print("Deleting moved object...")
    delete_object(bucket_name, "examples/hello-moved.txt", project_id=project_id)

    try:
        os.remove(tmp_path)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()


