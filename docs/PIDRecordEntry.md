# PIDRecordEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pytypid_generated_client.models.pid_record_entry import PIDRecordEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PIDRecordEntry from a JSON string
pid_record_entry_instance = PIDRecordEntry.from_json(json)
# print the JSON string representation of the object
print(PIDRecordEntry.to_json())

# convert the object into a dict
pid_record_entry_dict = pid_record_entry_instance.to_dict()
# create an instance of PIDRecordEntry from a dict
pid_record_entry_from_dict = PIDRecordEntry.from_dict(pid_record_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


