from typing import Dict, List

from pytypid_generated_client.models import PIDRecord, PIDRecordEntry, SimplePidRecord


class SimpleRecord(SimplePidRecord):
    def to_record(self) -> PIDRecord:
        """Convert SimplePidRecord to PIDRecord."""
        entries: Dict[str, List[PIDRecordEntry]] = {}
        if self.record:
            for pair in self.record:
                key = pair.key
                if not key:
                    continue
                if key not in entries:
                    entries[key] = []
                entries[key].append(PIDRecordEntry(key=key, value=pair.value))
        return PIDRecord(pid=self.pid, entries=entries)
