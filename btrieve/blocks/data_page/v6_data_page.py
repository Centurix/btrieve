class V6DataPage:
    def __init__(self, records):
        self.records = records
    
    @classmethod
    def from_fcr_and_block(cls, fcr, block):
        data = block[6:]

        records = list()

        # Iterate over the records in the page
        for record in [data[i:i + fcr.record_physical_size] for i in range(
            0,
            int(fcr.page_records) * fcr.record_physical_size,
            fcr.record_physical_size
        )]:
            if ord(record[0:1]) > 0 or ord(record[1:2]) > 0:
                records.append(record[2:fcr.record_size + 2])

        return cls(records)
