import boto3


def gather_credentials_via_assume_role(account_id, role):
    role_arn = f'arn:aws:iam::{account_id}:role/{role}'
    client = boto3.client('sts')
    response = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName='AssumedRole'
    )
    return response['Credentials']


def with_role(account_id, role):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            credentials = gather_credentials_via_assume_role(account_id, role)      
            new_kwargs = {
                **kwargs,
                **{ 
                    'aws_access_key_id': credentials['AccessKeyId'],
                    'aws_secret_access_key': credentials['SecretAccessKey'],
                    'aws_session_token': credentials['SessionToken']
                }}
            return f(*args, **new_kwargs)
        return wrapped_f
    return wrap
