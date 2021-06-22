# Fetch GH Release Asset To S3 Bucket

This action downloads an asset (zip file) from a GitHub release and upload the zip file to S3 bucket.

## Inputs

### `token`

**Required** 
The GitHub token. Typically this will be `${{ secrets.GITHUB_TOKEN }}`

### `src_repo`

**Optional** 
The `org/repo` containing the release. Defaults is the current repo.

### `aws_access_key_id`

**Required** 
The AWS credential. For example, this should be `${{ secrets.aws_access_key_id}}` Please refer to https://docs.github.com/en/actions/reference/encrypted-secrets

### `aws_secret_access_key`

**Required** 
The AWS credential. For example, this should be `${{ secrets.aws_secret_access_key}` Please refer to https://docs.github.com/en/actions/reference/encrypted-secrets

### `s3_bucket`

**Required** 
The S3 bucket's name 

### `s3_bucket_folder` 
**Optional** 
The S3 bucket folder name 

### `version`
**Optional** 
The version of file need to upload to S3 bucket. For example, the download url is https://github.com/zack5208/testAction/archive/refs/tags/v1.zip . This will be `v1`
Defaults is point to the latest release version zip file.


## Example usage

```yaml
uses: zack5208/testAction@master
with:
  src_repo: "zack5208/testAction" # Optional  Default: this calling repo
  token: ${{ secrets.GITHUB_TOKEN }} # Required
  aws_access_key_id: ${{ secrets.aws_access_key_id}} # Required
  aws_secret_access_key: ${{ secrets.aws_secret_access_key} # Required
  s3_bucket: "bucket_name" # Required
  s3_bucket_folder: "bucket_folder_name" #Optional 
  version:  "v1" # Optional  Default: the lastest version
```

## Support

This action only supports Linux runners as this is a [docker container](https://docs.github.com/en/actions/creating-actions/about-actions#types-of-actions) action. If you encounter `Error: Container action is only supported on Linux` then you are using non-linux runner.