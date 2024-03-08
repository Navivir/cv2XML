import os
from . import aws_interaction
import threading


# Procesa el documento
def validate_document(entry_file_path):
    if not os.path.exists(entry_file_path):
        print("El archivo no existe.")
        return
    bucket_name = os.getenv('BUCKET_NAME')
    s3_file_path = 'Script_uploaded/' + os.path.basename(entry_file_path)

    # Subir el archivo al S3 y luego iniciar el proceso en un hilo separado
    if aws_interaction.upload_to_s3(entry_file_path, bucket_name, s3_file_path):
        threading.Thread(target=lambda: aws_interaction.wait_for_textract_job_completion(s3_file_path)).start()

