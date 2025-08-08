# BatchRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid_records** | [**List[PIDRecord]**](PIDRecord.md) |  | [optional] 
**mapping** | **Dict[str, str]** |  | [optional] 

## Example

```python
from pytypid_generated_client.models.batch_record_response import BatchRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRecordResponse from a JSON string
batch_record_response_instance = BatchRecordResponse.from_json(json)
# print the JSON string representation of the object
print(BatchRecordResponse.to_json())

# convert the object into a dict
batch_record_response_dict = batch_record_response_instance.to_dict()
# create an instance of BatchRecordResponse from a dict
batch_record_response_from_dict = BatchRecordResponse.from_dict(batch_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


