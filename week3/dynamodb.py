import time
import boto3
import json
import pandas as pd
from decimal import Decimal

class DynamoDB:
    def __init__(self):
        boto3.setup_default_session(profile_name="corca-hasan", region_name="ap-northeast-3")
        resource = boto3.resource("dynamodb", region_name="ap-northeast-3")
        self.table = resource.Table("taehee-dynamo")

    def put_item(self, key):
        return self.table.put_item(Item=key)
    
    def get_item(self, key):
        return self.table.get_item(Key=key)
    
    def delete_item(self, key):
        return self.table.delete_item(Key=key)

if __name__ == "__main__":
    dynamodb_client = DynamoDB()
    table = dynamodb_client.table
    
    df = json.loads(
        pd.read_csv("titanic.csv").to_json(orient="records"), parse_float=Decimal
    )
    start = time.time()
    for i in df:
        table.put_item(Item=i)
    end = time.time()
    
    print(f"Upload records to dynamodb: {end - start} seconds")
    print(f"Upload records to dynamodb: {(end - start) / len(df)} seconds per record")