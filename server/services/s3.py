import boto3
# import os
from server import keys
bucket_name = 'cymetria-server-bucket'

def connect_s3():
    session_aws = boto3.Session(keys.ACCESS_KEY, keys.SECRET_KEY)
    # session_aws = boto3.Session(os.getenv('ACCESS_KEY'), os.getenv('SECRET_KEY'))
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_file(session_s3):    
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    for obj in bucket_objects:
        print(obj.key)
    print(bucket_objects)

def save_file(id, photo):
    extension = photo.filename.split(".")[1]
    email = id.split(".")[0]
    photo_name = email.replace('@','_') + "." + extension
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    return photo_path, photo_name

def upload_file(session_s3, photo_path, photo_name):
    path_photo_local = "profile_img/" + photo_name
    session_s3.meta.client.upload_file(photo_path, bucket_name, path_photo_local)
    url = "https://%s.s3.us-east-2.amazonaws.com/%s/%s" % (bucket_name,'profile_img', photo_name)
    return url




