from typing import Dict, List

from openapi_client.models import SimplePidRecord, SimplePair
from openapi_client.models import PIDRecord, PIDRecordEntry

class SimpleRecord(SimplePidRecord):
    def to_record(self) -> PIDRecord:
        """Convert SimplePidRecord to PIDRecord."""
        entries: Dict[str, List[PIDRecordEntry]] = {}
        if self.record:
            for pair in self.record:
                key = pair.key
                if key not in entries:
                    entries[key] = []
                entries[key].append(PIDRecordEntry(key=key, value=pair.value))
        return PIDRecord(pid=self.pid, entries=entries)
    
    def get_mime_type(self) -> str:
        """Return the MIME type for SimpleRecord."""
        return "application/vnd.datamanager.pid.simple+json"