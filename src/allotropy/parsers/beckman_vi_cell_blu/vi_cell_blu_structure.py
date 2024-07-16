from __future__ import annotations

import pandas as pd

from allotropy.allotrope.schema_mappers.adm.cell_counting.benchling._2023._11.cell_counting import (
    Data,
    Measurement,
    MeasurementGroup,
    Metadata,
)
from allotropy.parsers.beckman_vi_cell_blu.constants import (
    DEFAULT_ANALYST,
    DEFAULT_MODEL_NUMBER,
    VICELL_BLU_SOFTWARE_NAME,
)
from allotropy.parsers.utils.uuids import random_uuid_str
from allotropy.parsers.utils.values import (
    try_float_from_series,
    try_float_from_series_or_none,
    try_str_from_series,
    try_str_from_series_or_none,
)


def _create_measurement_group(data: pd.Series[str]) -> MeasurementGroup:
    total_cell_count = try_float_from_series_or_none(data, "Cell count")
    total_cell_count = (
        total_cell_count if total_cell_count is None else round(total_cell_count)
    )
    viable_cell_count = try_float_from_series_or_none(data, "Viable cells")
    viable_cell_count = (
        viable_cell_count if viable_cell_count is None else round(viable_cell_count)
    )

    return MeasurementGroup(
        measurements=[
            Measurement(
                measurement_identifier=random_uuid_str(),
                timestamp=try_str_from_series(data, "Analysis date/time"),
                sample_identifier=try_str_from_series(data, "Sample ID"),
                cell_type_processing_method=try_str_from_series_or_none(
                    data, "Cell type"
                ),
                minimum_cell_diameter_setting=try_float_from_series_or_none(
                    data, "Minimum Diameter (μm)"
                ),
                maximum_cell_diameter_setting=try_float_from_series_or_none(
                    data, "Maximum Diameter (μm)"
                ),
                cell_density_dilution_factor=try_float_from_series_or_none(
                    data, "Dilution"
                ),
                viability=try_float_from_series(data, "Viability (%)"),
                viable_cell_density=try_float_from_series(
                    data, "Viable (x10^6) cells/mL"
                ),
                total_cell_count=total_cell_count,
                total_cell_density=try_float_from_series_or_none(
                    data, "Total (x10^6) cells/mL"
                ),
                average_total_cell_diameter=try_float_from_series_or_none(
                    data, "Average diameter (μm)"
                ),
                average_live_cell_diameter=try_float_from_series_or_none(
                    data, "Average viable diameter (μm)"
                ),
                viable_cell_count=viable_cell_count,
                average_total_cell_circularity=try_float_from_series_or_none(
                    data, "Average circularity"
                ),
                average_viable_cell_circularity=try_float_from_series_or_none(
                    data, "Average viable circularity"
                ),
                analyst=try_str_from_series_or_none(data, "Analysis by")
                or DEFAULT_ANALYST,
            )
        ]
    )


def _create_measurement_groups(data: pd.DataFrame) -> list[MeasurementGroup]:
    return list(
        data.apply(
            _create_measurement_group, axis="columns"
        )  # type:ignore[call-overload]
    )


def create_data(data: pd.DataFrame) -> Data:
    metadata = Metadata(
        device_type="brightfield imager (cell counter)",
        detection_type="brightfield",
        model_number=DEFAULT_MODEL_NUMBER,
        software_name=VICELL_BLU_SOFTWARE_NAME,
    )

    return Data(metadata, _create_measurement_groups(data))
