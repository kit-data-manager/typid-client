# SimplePidRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** |  | [optional] 
**record** | [**List[SimplePair]**](SimplePair.md) |  | [optional] 

## Example

```python
from pytypid_generated_client.models.simple_pid_record import SimplePidRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePidRecord from a JSON string
simple_pid_record_instance = SimplePidRecord.from_json(json)
# print the JSON string representation of the object
print(SimplePidRecord.to_json())

# convert the object into a dict
simple_pid_record_dict = simple_pid_record_instance.to_dict()
# create an instance of SimplePidRecord from a dict
simple_pid_record_from_dict = SimplePidRecord.from_dict(simple_pid_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


