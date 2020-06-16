import boto3


def delete_member(pname, ptype):
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = dynamodb.Table('Project_Hxy')
    response = table.delete_item(
        Key={'projectName': pname, 'projectType': ptype},
        ConditionExpression='memberName = :val',
        ExpressionAttributeValues={
            ":val": 'Karl'
        }
    )
    return response


if __name__ == '__main__':
    delete_member('.Net2', '7')
    print('delete successful')
