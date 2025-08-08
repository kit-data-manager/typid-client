# TabulatorPaginationFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from pytypid_generated_client.models.tabulator_pagination_format import TabulatorPaginationFormat

# TODO update the JSON string below
json = "{}"
# create an instance of TabulatorPaginationFormat from a JSON string
tabulator_pagination_format_instance = TabulatorPaginationFormat.from_json(json)
# print the JSON string representation of the object
print(TabulatorPaginationFormat.to_json())

# convert the object into a dict
tabulator_pagination_format_dict = tabulator_pagination_format_instance.to_dict()
# create an instance of TabulatorPaginationFormat from a dict
tabulator_pagination_format_from_dict = TabulatorPaginationFormat.from_dict(tabulator_pagination_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


