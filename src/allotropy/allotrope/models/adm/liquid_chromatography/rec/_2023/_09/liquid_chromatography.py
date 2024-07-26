# generated by datamodel-codegen:
#   filename:  liquid-chromatography.schema.json
#   timestamp: 2024-07-18T20:03:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCentimeter,
    TQuantityValueCounts,
    TQuantityValueCountsTimesSecond,
    TQuantityValueCubicMillimeter,
    TQuantityValueHertz,
    TQuantityValueMicrometer,
    TQuantityValueMilliAbsorbanceUnit,
    TQuantityValueMilliAbsorbanceUnitTimesMilliliter,
    TQuantityValueMilliAbsorbanceUnitTimesSecond,
    TQuantityValueMilliliter,
    TQuantityValueMillimeter,
    TQuantityValueMillivolt,
    TQuantityValueMillivoltTimesSecond,
    TQuantityValueNanoCoulomb,
    TQuantityValueNanoCoulombTimesSecond,
    TQuantityValueNanometer,
    TQuantityValuePercent,
    TQuantityValuePicoAmpere,
    TQuantityValuePicoAmpereTimesSecond,
    TQuantityValueSecondTime,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TClass,
    TDatacube,
    TDateTimeStampValue,
    TDateTimeValue,
    TQuantityValue,
    TStringValue,
)


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None


@dataclass(kw_only=True)
class AdmCoreREC202309ManifestSchema:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass(kw_only=True)
class OrderedItem:
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]


@dataclass(kw_only=True)
class StatisticsDocumentItem:
    statistical_feature: TClass


@dataclass(kw_only=True)
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None
    pump_model_number: TStringValue | None = None
    detector_model_number: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    detection_type: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    model_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    field_index: int | None = None
    detector_offset_setting: TQuantityValue | None = None
    detector_sampling_rate_setting: TQuantityValueHertz | None = None
    detector_wavelength_setting: TQuantityValueNanometer | None = None
    detector_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = (
        None
    )
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    batch_identifier: TStringValue | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None


@dataclass(kw_only=True)
class PeakItem:
    peak_end: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    identifier: TStringValue | None = None
    relative_peak_height: TQuantityValuePercent | None = None
    written_name: TStringValue | None = None
    peak_height: TQuantityValueCounts | TQuantityValueMillivolt | TQuantityValueNanoCoulomb | TQuantityValuePicoAmpere | None = (
        None
    )
    capacity_factor__chromatography_: TQuantityValueUnitless | None = None
    peak_area: TQuantityValueCountsTimesSecond | TQuantityValueMillivoltTimesSecond | TQuantityValueNanoCoulombTimesSecond | TQuantityValuePicoAmpereTimesSecond | None = (
        None
    )
    relative_peak_area: TQuantityValuePercent | None = None
    retention_time: TQuantityValueSecondTime | None = None
    retention_volume: TQuantityValueMilliliter | None = None
    peak_start: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    peak_selectivity__chromatography_: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_baseline_peak_widths: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_statistical_moments: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates__chromatography_: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_60_7___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_32_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_13_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_4_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_tangent_method: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_by_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height__JP14_: TQuantityValueUnitless | None = (
        None
    )
    peak_width_at_4_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_13_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_32_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_60_7___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_half_height: TQuantityValueSecondTime | None = None
    peak_width_at_5___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_baseline: TQuantityValueSecondTime | None = None
    peak_width_at_inflection: TQuantityValueSecondTime | None = None
    peak_width_at_10___of_height: TQuantityValueSecondTime | None = None
    peak_width: TQuantityValueSecondTime | None = None
    statistical_skew__chromatography_: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_5___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_10___height: TQuantityValueUnitless | None = None
    asymmetry_factor_squared_measured_at_10___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_squared_measured_at_4_4___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_measured_at_4_4___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_baseline: TQuantityValueUnitless | None = None
    chromatographic_peak_asymmetry_factor: TQuantityValueUnitless | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class PeakList:
    peak: list[PeakItem] | None = None


@dataclass(kw_only=True)
class ProcessedDataDocumentItem:
    data_processing_document: dict[str, Any] | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None
    peak_list: PeakList | None = None


@dataclass(kw_only=True)
class ChromatographyColumnDocument:
    chromatography_column_part_number: TStringValue | None = None
    chromatography_column_serial_number: TStringValue | None = None
    chromatography_column_length: TQuantityValueCentimeter | None = None
    column_inner_diameter: TQuantityValueMillimeter | None = None
    chromatography_column_chemistry_type: TStringValue | None = None
    chromatography_column_particle_size: TQuantityValueMicrometer | None = None
    product_manufacturer: TStringValue | None = None


@dataclass(kw_only=True)
class InjectionDocument:
    autosampler_injection_volume_setting__chromatography_: TQuantityValueCubicMillimeter
    injection_identifier: TStringValue
    injection_time: TDateTimeValue


@dataclass(kw_only=True)
class PeakItem1(OrderedItem):
    peak_height: TQuantityValue | None = None
    peak_area: TQuantityValue | None = None


@dataclass(kw_only=True)
class PeakList1:
    peak: list[PeakItem1] | None = None


@dataclass(kw_only=True)
class ProcessedDataDocument:
    peak_list: PeakList1 | None = None


@dataclass(kw_only=True)
class PeakItem11(OrderedItem):
    peak_height: TQuantityValueMilliAbsorbanceUnit | None = None
    peak_area: TQuantityValueMilliAbsorbanceUnitTimesMilliliter | TQuantityValueMilliAbsorbanceUnitTimesSecond | None = (
        None
    )


@dataclass(kw_only=True)
class PeakList11:
    peak: list[PeakItem11] | None = None


@dataclass(kw_only=True)
class ProcessedDataDocument11:
    peak_list: PeakList11 | None = None


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class MeasurementDocument:
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    chromatography_column_document: ChromatographyColumnDocument
    measurement_time: TDateTimeStampValue | None = None
    measurement_identifier: TStringValue | None = None
    detection_type: TStringValue | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    injection_document: InjectionDocument | None = None
    chromatogram_data_cube: TDatacube | None = None
    three_dimensional_ultraviolet_spectrum_data_cube: TDatacube | None = None
    processed_data_document: ProcessedDataDocument | ProcessedDataDocument11 | None = (
        None
    )
    mass_chromatogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocument]
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class LiquidChromatographyDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class LiquidChromatographyAggregateDocument:
    liquid_chromatography_document: list[LiquidChromatographyDocumentItem]
    device_system_document: DeviceSystemDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    field_asm_manifest: AdmCoreREC202309ManifestSchema | str
    liquid_chromatography_aggregate_document: LiquidChromatographyAggregateDocument | None = (
        None
    )
