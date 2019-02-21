import boto3
import urllib
import click


@click.command()
@click.option("--assume-role")
@click.option("--function-name", required=True)
@click.option("--s3-url", required=True)
@click.option("--region-name", default=None, required=False)
def main(assume_role, function_name, s3_url):
    client = get_client(assume_role)
    s3_url_info = urllib.parse.urlparse(s3_url)

    response = client.update_function_code(
        FunctionName=function_name,
        S3Bucket=s3_url_info.netloc,
        S3Key=s3_url_info.path[1:],
        Publish=True,
        DryRun=False,
    )
    print(response)


def get_client(assume_role, region_name):
    credentials = {}
    if assume_role:
        sts = boto3.client("sts")
        resp = sts.assume_role(RoleArn=assume_role, RoleSessionName="aws-lambda-deploy")
        credentials.update(
            {
                "aws_secret_access_key": resp["Credentials"]["SecretAccessKey"],
                "aws_access_key_id": resp["Credentials"]["AccessKeyId"],
                "aws_session_token": resp["Credentials"]["SessionToken"],
            }
        )

    if region_name:
        credentials.update({"region_name": region_name})

    return boto3.client("lambda", **credentials)


if __name__ == "__main__":
    main()
