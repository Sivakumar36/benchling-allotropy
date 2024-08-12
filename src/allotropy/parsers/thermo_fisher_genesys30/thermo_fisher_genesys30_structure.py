from __future__ import annotations

import io
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd
import pytz

from allotropy.allotrope.models.adm.spectrophotometry.benchling._2023._12.spectrophotometry import ContainerType
from allotropy.allotrope.models.shared.definitions.custom import TQuantityValueNanometer
from allotropy.allotrope.models.shared.definitions.definitions import FieldComponentDatatype
from allotropy.allotrope.pandas_util import read_csv, read_excel
from allotropy.constants import DEFAULT_ENCODING
from allotropy.named_file_contents import NamedFileContents
from allotropy.parsers.lines_reader import LinesReader, read_to_lines
import pandas as pd

from allotropy.parsers.thermo_fisher_genesys30 import constants
from allotropy.parsers.utils.pandas import map_rows, SeriesData, df_to_series_data
# from allotropy.parsers.vendor_parser import _get_date_time
from allotropy.parsers.utils.units import get_quantity_class
from allotropy.parsers.constants import NOT_APPLICABLE
from allotropy.allotrope.schema_mappers.adm.spectrophotometry.benchling._2023._12.spectrophotometry import (
    CalculatedDataItem,
    Mapper,
    Data,
    DataSource,
    Measurement,
    MeasurementGroup,
    Metadata,
    ProcessedData,
    ProcessedDataFeature, MeasurementType, DataCube, DataCubeComponent,
)
from allotropy.parsers.utils.uuids import random_uuid_str
from allotropy.parsers.utils.pandas import map_rows, SeriesData

def _get_value(data_frame: pd.DataFrame, column: str) -> Any | None:
    """
    Retrieves the value from a specified column and row in a DataFrame, handling NaNs
    and converting certain numpy types to native Python types.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame from which to retrieve the value.
    column (str): The column name from which to retrieve the value.
    row (int): The row index from which to retrieve the value.

    Returns:
    Optional[Any|None]: The value from the specified cell converted to the appropriate Python type.
                   Returns None if the column does not exist or the value is NaN.
    """
    for row in range(len(data_frame.index)):
        if column not in data_frame.columns:
            return None
        value = data_frame[column][row]

        if pd.isna(value):
            return None
        if isinstance(value, np.int64):
            return int(value)
        if isinstance(value, np.float64):
            return float(value)
        return value


def create_data(named_file_contents: NamedFileContents):
    lines = read_to_lines(named_file_contents)
    reader = LinesReader(lines)
    lines = [line for line in reader.pop_until("^,,") if line]
    # for line_ in lines:
    #     print("lines",line_)
    reader.drop_until_inclusive(",,")
    data_lines_after = list(reader.pop_until_empty())
    # for line in data_lines_after:
    #     print(line)

    # df_after = lines_to_df(data_lines_after)
    csv_string = "\n".join(data_lines_after)

    # Use StringIO to create a file-like object from the string
    csv_file_like = io.StringIO(csv_string)

    # Read the CSV data into a DataFrame
    rawdata_dataframe=pd.read_csv(csv_file_like,header=0)
    print("\nData after ,, DataFrame:")
    print(rawdata_dataframe)

    if named_file_contents.original_file_name.endswith(".csv"):
        metadata_dataframe = pd.read_csv(
            io.StringIO("\n".join(lines)),
            header=None,
            # index_col=0,
            keep_default_na=False,
        ).T
    else:
        metadata_dataframe = pd.read_csv(
            io.StringIO("\n".join(lines)),
            header=None,
            # index_col=0,
            keep_default_na=False,
            sep="\t",
        ).T

    metadata_dataframe.columns = metadata_dataframe.iloc[0]

    # Drop the first row which is now the header
    transposed_metadata_dataframe = metadata_dataframe[1:]

    # Reset index for clean DataFrame
    transposed_metadata_dataframe.reset_index(drop=True, inplace=True)

    print("transposed data\n",transposed_metadata_dataframe)

    data = df_to_series_data(transposed_metadata_dataframe, "Failed to parser header data")
    print(data)
    # rawdata = df_to_series_data(rawdata_dataframe, "Failed to parser header data")
    experiment_type_with_datetime = data.get(str, "Scan")
    print("exp---", experiment_type_with_datetime)
    exp_type, datetime_str = experiment_type_with_datetime.split('_', 1)
    datetime_str = datetime_str.split('.')[0]  # Remove the file extension if any

    # Step 2: Extract date and time components
    date_str = datetime_str[:8]  # '20230914'
    time_str = datetime_str[9:]  # '160142'
    print(date_str, time_str)
    # Combine date and time
    combined_str = date_str + time_str  # '20230914160142'

    # Step 3: Parse the combined date-time string
    datetime_obj = datetime.strptime(combined_str, '%Y%m%d%H%M%S')
    datetime_str = datetime_obj.strftime("%d-%m-%Y %I:%M %p")
    print(datetime_str)
    # Step 4: Convert to ISO 8601 format with timezone (UTC)
    # datetime_obj_utc = datetime_obj.replace(tzinfo=pytz.UTC)
    # iso_format = datetime_obj_utc.isoformat()
    # print(iso_format)
    file_name = named_file_contents.original_file_name
    data_data=Data(
        metadata=Metadata(
            file_name=file_name,
            device_type=constants.DEVICE_TYPE,
            device_identifier=NOT_APPLICABLE,
            model_number=constants.MODEL_NUMBER,
            software_name=constants.GENESYS_SOFTWARE,
            detection_type=data.get(str, "Mode"),
            product_manufacturer=constants.PRODUCT_MANUFACTURER,
            brand_name=constants.BRAND_NAME,
            container_type=ContainerType.tube,
        ),
        measurement_groups=[MeasurementGroup(
            measurement_time=datetime_str,
            experiment_type=exp_type,
            measurements=[
                Measurement(
                    type_=MeasurementType.ULTRAVIOLET_ABSORBANCE_SPECTRUM,
                    identifier=random_uuid_str(),
                    sample_identifier=NOT_APPLICABLE,
                    operating_minimum=data.get(str, "Lower"),
                    operating_maximum=data.get(str, "Upper"),
                ),
            ],
        ),
        ],
    )
    print(data_data)
    return Data(
        metadata=Metadata(
            file_name=file_name,
            device_type=constants.DEVICE_TYPE,
            device_identifier=NOT_APPLICABLE,
            model_number=constants.MODEL_NUMBER,
            software_name=constants.GENESYS_SOFTWARE,
            detection_type=data.get(str, "Mode"),
            product_manufacturer=constants.PRODUCT_MANUFACTURER,
            brand_name=constants.BRAND_NAME,
            container_type=ContainerType.tube,
        ),
        measurement_groups=[MeasurementGroup(
            measurement_time=datetime_str,
            experiment_type=exp_type,
            measurements=[
                Measurement(
                    type_=MeasurementType.ULTRAVIOLET_ABSORBANCE_SPECTRUM,
                    identifier=random_uuid_str(),
                    sample_identifier=NOT_APPLICABLE,
                    operating_minimum=data.get(str, "Lower"),
                    operating_maximum=data.get(str, "Upper"),
                    data_cube=DataCube(
                        label="absorption spectrum",
                        structure_dimensions=[DataCubeComponent(
                            type_=FieldComponentDatatype.double,
                            concept="wavelength",
                            unit="nm",
                        )],
                        structure_measures=[DataCubeComponent(
                            type_=FieldComponentDatatype.double,
                            concept="absorbance",
                            unit="mAU",
                        )],
                        dimensions=[[_get_value(rawdata_dataframe,"wavelength(nm)")]],
                        measures=[[_get_value(rawdata_dataframe,"ABS")]],

                ),
                ),
            ],
        ),
        ],
    )

# @staticmethod
# def create_data(data: pd.DataFrame) -> list[Row]:
#     return map_rows(data, Row.create_data)
