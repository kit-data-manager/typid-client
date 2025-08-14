# coding: utf-8

import unittest

from test.test_pid_management_api import TestPIDManagementApi as BaseTestPIDManagementApi

from pytypid import SimpleRecord, BatchRecordResponse


class TestPIDManagementApi(BaseTestPIDManagementApi):
    """PIDManagementApi unit test stubs"""

    def test_create_pid(self) -> None:
        """Test case for create_pid

        Create a new PID record
        """
        input = SimpleRecord.from_dict({
            "record": [
                { "key": "21.T11148/c692273deb2772da307f", "value": "1.0.0" }
            ]
        })

        assert input is not None, "Input should not be None"

        result = self.api.create_pid(
            pid_record=input.to_record()
        )

        print("Created:", result.to_json())
        assert result is not None, "Result should not be None"
        assert result.pid is not None, "PID should be set in the result"
        assert "21.T11148/c692273deb2772da307f" in result.to_str()

    def test_create_pids(self) -> None:
        """Test case for create_pids

        Create a multiple, possibly related PID records
        """
        input1 = SimpleRecord.from_dict({
            "pid": "a",
            "record": [
                { "key": "21.T11148/d0773859091aeb451528", "value": "b" }
            ]
        })

        input2 = SimpleRecord.from_dict({
            "pid": "b",
            "record": [
                { "key": "21.T11148/d0773859091aeb451528", "value": "a" }
            ]
        })

        assert input1 is not None, "Input1 should not be None"
        assert input2 is not None, "Input2 should not be None"

        result: BatchRecordResponse = self.api.create_pids(
            pid_record=[input1.to_record(), input2.to_record()]
        )

        assert result is not None, "Result should not be None"
        assert result.pid_records is not None, "PID records should not be None"
        assert len(result.pid_records) == 2, "There should be two PID records created"

        a = result.pid_records[0]
        b = result.pid_records[1]

        assert a.entries is not None, "Entries for PID 'a' should not be None"
        assert b.entries is not None, "Entries for PID 'b' should not be None"

        assert len(a.entries) == 1, "PID 'a' should have one entry"
        assert len(b.entries) == 1, "PID 'b' should have one entry"

        assert a.entries["21.T11148/d0773859091aeb451528"][0].value == b.pid, \
            "Value for PID 'a' should be 'b'"
        assert b.entries["21.T11148/d0773859091aeb451528"][0].value == a.pid, \
            "Value for PID 'b' should be 'a'"

if __name__ == '__main__':
    unittest.main()
