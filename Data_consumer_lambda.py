import json
import boto3
import base64
firehose_client = boto3.client('firehose')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    for partition_key in event['records']:
        #print('partition_key ', partition_key)
        partition_value = event['records'][partition_key]
        #print('partition_value ', partition_value)
        for record_value in partition_value:
            actual_message = (base64.b64decode(record_value['value']).decode('utf-8'))
            #print(actual_message)
            new_image = json.dumps({actual_message:'this is attached from consumer lambda!'}).encode('utf-8')
            #print(new_image)
            try:
                response = firehose_client.put_record(
                    DeliveryStreamName='<Your-Firehose_stream-Name>',
                    Record={
                        'Data': new_image
                        }
                    )
            except Exception as e:
                print('error', e)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                print('success')
            else:
                print('failed')

