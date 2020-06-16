import boto3


def get_member(pname, ptype):
    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-1')
    response = dynamodb.transact_get_items(
        TransactItems=[
            {
                'Get': {
                    'Key': {
                        "projectName": {
                            "S": pname
                        },
                        "projectType": {
                            "S": ptype
                        },
                    },
                    'TableName': 'Project_Hxy',
                }
            }
        ])

    # Key={'projectName': pname, 'projectType': ptype})
    return response['Responses']


if __name__ == '__main__':
    member = get_member('GO', '2')
    print('The memberName is %s' % member[0]["Item"]["memberName"]["S"])

    # membername = member.memberName
