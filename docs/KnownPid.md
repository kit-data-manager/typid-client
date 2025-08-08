# KnownPid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** |  | 
**created** | **datetime** |  | 
**modified** | **datetime** |  | 

## Example

```python
from pytypid_generated_client.models.known_pid import KnownPid

# TODO update the JSON string below
json = "{}"
# create an instance of KnownPid from a JSON string
known_pid_instance = KnownPid.from_json(json)
# print the JSON string representation of the object
print(KnownPid.to_json())

# convert the object into a dict
known_pid_dict = known_pid_instance.to_dict()
# create an instance of KnownPid from a dict
known_pid_from_dict = KnownPid.from_dict(known_pid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


