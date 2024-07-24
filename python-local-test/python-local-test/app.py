import json
import pandas as pd

def lambda_handler(event, context):
    count = event['count']
    data = []
    
    for i in range(count):
        data.append(i * 10)
        
    df = pd.DataFrame(data, columns=['Numbers'])
    
    print('Data:')
    print(df)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "statusCode": 200,
            "message": "Success",
            "Count": count
        })
    }

