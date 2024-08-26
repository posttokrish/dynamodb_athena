import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('athena')
    config_client = boto3.client('config')

    workgroups = client.list_work_groups()
    evaluations = []

    for wg in workgroups['WorkGroups']:
        wg_name = wg['Name']
        wg_info = client.get_work_group(WorkGroup=wg_name)
        encryption_config = wg_info['WorkGroup']['Configuration']['ResultConfiguration']['EncryptionConfiguration']

        compliance_type = 'NON_COMPLIANT'
        if encryption_config.get('EncryptionOption') == 'SSE_KMS' and encryption_config.get('KmsKey') is not None:
            compliance_type = 'COMPLIANT'

        evaluations.append({
            'ComplianceResourceType': 'AWS::Athena::WorkGroup',
            'ComplianceResourceId': wg_name,
            'ComplianceType': compliance_type,
            'Annotation': f'Athena Workgroup {wg_name} is {compliance_type}.',
            'OrderingTimestamp': event['invokingEvent']['notificationCreationTime']
        })

    config_client.put_evaluations(
        Evaluations=evaluations,
        ResultToken=event['resultToken']
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Evaluation complete.')
    }

