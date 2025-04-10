

from django.db.models.signals import post_save
from django.dispatch import receiver
import subprocess
import os

from utility.models import FileDetail, File_Electric, UtilityBillUpload

@receiver(post_save, sender=FileDetail)
def sync_json_file(sender, instance, created, **kwargs):
    if instance.file_path:
        local_path = instance.file_path.path  
        filename = os.path.basename(local_path)
        remote_dir = "/path/to/remote/json_uploads/" 
        remote_path = f"username@192.168.45.230:{remote_dir}"
        
        
        subprocess.call(['ssh', 'username@192.168.45.230', f'mkdir -p {remote_dir}'])
        
        
        subprocess.call(['rsync', '-avz', local_path, remote_path])
        print(f"Synced {local_path} to {remote_path}")

@receiver(post_save, sender=File_Electric)
def sync_electric_file(sender, instance, created, **kwargs):
    if instance.file_path:
        local_path = instance.file_path.path
        filename = os.path.basename(local_path)
        remote_dir = "/path/to/remote/electric_json_uploads/"
        remote_path = f"username@192.168.45.230:{remote_dir}"
        
        subprocess.call(['ssh', 'username@192.168.45.230', f'mkdir -p {remote_dir}'])
        subprocess.call(['rsync', '-avz', local_path, remote_path])
        print(f"Synced {local_path} to {remote_path}")

@receiver(post_save, sender=UtilityBillUpload)
def sync_utility_file(sender, instance, created, **kwargs):
    if instance.file:
        local_path = instance.file.path
        filename = os.path.basename(local_path)
        remote_dir = "/path/to/remote/uploads/"
        remote_path = f"username@192.168.45.230:{remote_dir}"
        
        subprocess.call(['ssh', 'username@192.168.45.230', f'mkdir -p {remote_dir}'])
        subprocess.call(['rsync', '-avz', local_path, remote_path])
        print(f"Synced {local_path} to {remote_path}")