import boto3


def put_item(pname, ptype, mname):
    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-1')
    response = dynamodb.transact_write_items(
        TransactItems=[
            {
                'Put': {
                    'TableName': 'Project_Hxy',
                    'Item': {
                        "Active": {
                            "BOOL": True
                        },
                        "comment": {
                            "NULL": True
                        },
                        "info": {
                            "M": {
                                "ID": {
                                    "L": [
                                        {
                                            "N": "23"
                                        },
                                        {
                                            "S": "male"
                                        }
                                    ]
                                }
                            }
                        },
                        "memberName": {
                            "S": mname
                        },
                        "Photo": {
                            "B": "test"
                        },
                        "projectName": {
                            "S": pname
                        },
                        "projectType": {
                            "S": ptype
                        },
                        "startDate": {
                            "S": "2020-5-21"
                        }
                    },
                }
            }
        ]
    )
    return response


if __name__ == '__main__':
    put_item('.Net3', '10', 'Karl')
    print('add successful')
