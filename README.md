# Fetch GH Release Asset To S3 Bucket

This action downloads an asset (zip file) from a GitHub release and upload the zip file to S3 bucket.

## Inputs

### `token`

**Required** The GitHub token. Typically this will be `${{ secrets.GITHUB_TOKEN }}`

### `repo`

**Required** The `org/repo` containing the release. 

### `aws_access_key_id`

**Required** The AWS credential. For example, this should be `${{ secrets.aws_access_key_id}}` Please refer to https://docs.github.com/en/actions/reference/encrypted-secrets

### `aws_secret_access_key`

**Required** The AWS credential. For example, this should be `${{ secrets.aws_secret_access_key}` Please refer to https://docs.github.com/en/actions/reference/encrypted-secrets

### `aws_session_token`

**Required** The AWS credential. For example, this should be `${{ secrets.aws_session_token}` Please refer to https://docs.github.com/en/actions/reference/encrypted-secrets


## Example usage

```yaml
uses: zack5208/testAction@master
with:
  repo: "zack5208/testAction"
  token: ${{ secrets.GITHUB_TOKEN }}
  aws_access_key_id: ${{ secrets.aws_access_key_id}}
  aws_secret_access_key: ${{ secrets.aws_secret_access_key}
  aws_session_token: ${{ secrets.aws_session_token}
  s3_bucket: "bucket_name"
```

## Support

This action only supports Linux runners as this is a [docker container](https://docs.github.com/en/actions/creating-actions/about-actions#types-of-actions) action. If you encounter `Error: Container action is only supported on Linux` then you are using non-linux runner.