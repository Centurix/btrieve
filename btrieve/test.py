#!/usr/bin/env python3
import os
import struct
import click
from blocks import (
    FileControlRecordFactory,
    PageAllocationTableFactory,
    DataPageFactory,
    PointerTypes
)
from records import (
    FieldFactory,
    TableFactory
)


DB_FOLDER = "samples/DDF2006"  # V6
# DB_FOLDER = "samples/DDFOld"  # V6
# DB_FOLDER = "samples/TRYDDF"  # V6

# DB_FOLDER = "samples/DDF20170515"  # V8
# DB_FOLDER = "samples/WinTgs11"  # V8
BLOCK_SIZE = 256

def total_pat_pages(file_size, page_size):
    return (file_size + 130 * page_size) // (130 * page_size)

def pat_offset(pat_number, page_size):
    return (128 * pat_number + 2) * page_size


def raw_records(file_path):
    data_file_size = os.path.getsize(file_path)

    records = list()

    with open(file_path, "rb") as data:
        # Read the FCR block
        block_1 = data.read(BLOCK_SIZE)
        block_2 = data.read(BLOCK_SIZE)

        fcr = FileControlRecordFactory.from_blocks(block_1, block_2)
        pat_pages = total_pat_pages(data_file_size, fcr.page_size)

        # Go get some data from the Page Allocation Table
        for pat_count in range(0, int(pat_pages)):
            offset = pat_offset(pat_count, fcr.page_size)

            data.seek(offset)
            pat = PageAllocationTableFactory.from_blocks(
                data.read(fcr.page_size), 
                data.read(fcr.page_size)
            )

            for pointer in pat.pointers:
                if pointer[0] == PointerTypes.DATA:
                    data.seek(pointer[1] * fcr.page_size)
                    data_page = data.read(fcr.page_size)
                    page = DataPageFactory.from_fcr_and_block(fcr, data_page)
                    records += page.records

    return records


def get_fields(folder):
    field_file_path = os.path.join(DB_FOLDER, "FIELD.DDF")
    
    table_fields = dict()

    for record in raw_records(field_file_path):
        field_meta = FieldFactory.from_raw_record(record)
        if str(field_meta.file_id) not in table_fields:
            table_fields[str(field_meta.file_id)] = list()

        table_fields[str(field_meta.file_id)].append(field_meta)

    return table_fields


def get_tables(folder):
    table_file_path = os.path.join(DB_FOLDER, "FILE.DDF")

    tables = list()

    for record in raw_records(table_file_path):
        tables.append(TableFactory.from_raw_record(record))

    return tables

def get_indexes(folder):
    index_file_path = os.path.join(DB_FOLDER, "INDEX.DDF")

    indexes = list()
    for record in raw_records(index_file_path):
        indexes.append(record)

    return indexes

@click.command()
def main():
    click.echo(f"Extracting from {DB_FOLDER}...")

    fields = get_fields(DB_FOLDER)
    tables = get_tables(DB_FOLDER)
    indexes = get_indexes(DB_FOLDER)

    for table in tables:
        click.echo(table.table_name)

    # database = Database.from_metadata(tables, fields, indexes)

if __name__ == "__main__":
    main()
