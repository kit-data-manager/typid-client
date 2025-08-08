# PIDRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** |  | [optional] 
**entries** | **Dict[str, List[PIDRecordEntry]]** |  | [optional] 

## Example

```python
from pytypid_generated_client.models.pid_record import PIDRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PIDRecord from a JSON string
pid_record_instance = PIDRecord.from_json(json)
# print the JSON string representation of the object
print(PIDRecord.to_json())

# convert the object into a dict
pid_record_dict = pid_record_instance.to_dict()
# create an instance of PIDRecord from a dict
pid_record_from_dict = PIDRecord.from_dict(pid_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


