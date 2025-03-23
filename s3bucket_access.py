#%%
import boto3
s3bucket = boto3.resource('s3')

#%%
bucket = s3bucket.Bucket('ioostestbucket')
for obj in bucket.objects.all():
    print(obj)
# %%
# ensuring the ownership of account

# Create an STS client
sts_client = boto3.client('sts')

# Call get_caller_identity to get the AWS account ID
response = sts_client.get_caller_identity()
account_id = response['Account']
print(f"Connected to AWS Account ID: {account_id}")
# %%

# uploading a file to bucket
s3bucket2 = boto3.client('s3')
response =s3bucket2.upload_file(
            Filename='test.nc',
            Bucket='ioostestbucket',
            Key='test_ioos.nc')
        
# %%
