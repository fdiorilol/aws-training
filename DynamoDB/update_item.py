import boto3


def update_Active(pname, ptype, status):
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = dynamodb.Table('Project_Hxy')
    response = table.update_item(
        Key={'projectName': pname, 'projectType': ptype},
        UpdateExpression='set Active = :val',
        ExpressionAttributeValues={
            ":val": status
        },
        ReturnValues="UPDATED_NEW"
    )
    print('update %s to %s successful' % (pname, status))
    return response


if __name__ == '__main__':
    update_Active('GO', '2', 'false')
