from __future__ import annotations

import io
import os
from typing import Iterable, List, Optional

from google.cloud import storage


def _get_client(project_id: Optional[str] = None) -> storage.Client:
    """
    Create a Google Cloud Storage client.

    Relies on ADC (Application Default Credentials). Ensure one of the following:
    - `GOOGLE_APPLICATION_CREDENTIALS` points to a service account JSON key
    - `gcloud auth application-default login` has been run
    """
    return storage.Client(project=project_id) if project_id else storage.Client()


def upload_file(
    bucket_name: str,
    destination_blob_name: str,
    source_file_path: str,
    *,
    project_id: Optional[str] = None,
    content_type: Optional[str] = None,
) -> str:
    """
    Upload a local file to a GCS bucket.

    Returns the gs:// URI of the uploaded object.
    """
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path, content_type=content_type)
    return f"gs://{bucket_name}/{destination_blob_name}"


def upload_bytes(
    bucket_name: str,
    destination_blob_name: str,
    data: bytes,
    *,
    project_id: Optional[str] = None,
    content_type: Optional[str] = None,
) -> str:
    """
    Upload in-memory bytes as an object to GCS.

    Returns the gs:// URI of the uploaded object.
    """
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(io.BytesIO(data), size=len(data), content_type=content_type)
    return f"gs://{bucket_name}/{destination_blob_name}"


def download_file(
    bucket_name: str,
    source_blob_name: str,
    destination_file_path: str,
    *,
    project_id: Optional[str] = None,
) -> str:
    """
    Download a GCS object to a local file path.

    Returns the local path of the downloaded file.
    """
    os.makedirs(os.path.dirname(destination_file_path) or ".", exist_ok=True)
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
    return destination_file_path


def download_bytes(
    bucket_name: str,
    source_blob_name: str,
    *,
    project_id: Optional[str] = None,
) -> bytes:
    """
    Download a GCS object content as bytes.
    """
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    return blob.download_as_bytes()


def list_objects(
    bucket_name: str,
    prefix: str = "",
    *,
    project_id: Optional[str] = None,
) -> List[str]:
    """
    List object names in a bucket optionally filtered by prefix.
    """
    client = _get_client(project_id)
    blobs = client.list_blobs(bucket_name, prefix=prefix)
    return [blob.name for blob in blobs]


def get_metadata(
    bucket_name: str,
    blob_name: str,
    *,
    project_id: Optional[str] = None,
) -> dict:
    """
    Retrieve metadata for an object.
    """
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    if blob is None:
        raise FileNotFoundError(f"Object not found: gs://{bucket_name}/{blob_name}")
    return {
        "name": blob.name,
        "size": blob.size,
        "content_type": blob.content_type,
        "updated": blob.updated.isoformat() if blob.updated else None,
        "generation": blob.generation,
        "md5_hash": blob.md5_hash,
        "crc32c": blob.crc32c,
        "storage_class": blob.storage_class,
        "kms_key_name": blob.kms_key_name,
        "custom_time": blob.custom_time.isoformat() if blob.custom_time else None,
        "metadata": dict(blob.metadata or {}),
    }


def delete_object(
    bucket_name: str,
    blob_name: str,
    *,
    project_id: Optional[str] = None,
) -> None:
    """
    Delete an object from a bucket. No error if it does not exist.
    """
    client = _get_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    try:
        blob.delete()
    except Exception:
        # Suppress errors for idempotency when object doesn't exist or already deleted
        pass


def copy_object(
    source_bucket: str,
    source_blob: str,
    destination_bucket: str,
    destination_blob: str,
    *,
    project_id: Optional[str] = None,
) -> str:
    """
    Copy an object to another location (can be same bucket).

    Returns gs:// URI of the destination object.
    """
    client = _get_client(project_id)
    src_bucket = client.bucket(source_bucket)
    src_blob = src_bucket.blob(source_blob)
    dest_bucket = client.bucket(destination_bucket)
    dest_blob = src_bucket.copy_blob(src_blob, dest_bucket, destination_blob)
    return f"gs://{dest_blob.bucket.name}/{dest_blob.name}"


def move_object(
    source_bucket: str,
    source_blob: str,
    destination_bucket: str,
    destination_blob: str,
    *,
    project_id: Optional[str] = None,
) -> str:
    """
    Move (copy then delete) an object to another location.
    Returns gs:// URI of the destination object.
    """
    dest_uri = copy_object(
        source_bucket,
        source_blob,
        destination_bucket,
        destination_blob,
        project_id=project_id,
    )
    delete_object(source_bucket, source_blob, project_id=project_id)
    return dest_uri


__all__ = [
    "upload_file",
    "upload_bytes",
    "download_file",
    "download_bytes",
    "list_objects",
    "get_metadata",
    "delete_object",
    "copy_object",
    "move_object",
]


