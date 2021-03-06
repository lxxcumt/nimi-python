# This file was generated

from enum import Enum


class ADCCalibration(Enum):
    AUTO = -1
    '''
    The DMM enables or disables ADC calibration for you.
    '''
    OFF = 0
    '''
    The DMM does not compensate for changes to the gain.
    '''
    ON = 1
    '''
    The DMM measures an internal reference to calculate the correct gain for the  measurement.
    '''


class AcquisitionStatus(Enum):
    RUNNING = 0
    '''
    Running
    '''
    FINISHED_WITH_BACKLOG = 1
    '''
    Finished with **Backlog**
    '''
    FINISHED_WITH_NO_BACKLOG = 2
    '''
    Finished with no **Backlog**
    '''
    PAUSED = 3
    '''
    Paused
    '''
    NO_ACQUISITION_IN_PROGRESS = 4
    '''
    No acquisition in progress
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 0
    '''
    Seconds
    '''
    POWER_LINE_CYCLES = 1
    '''
    Powerline Cycles
    '''


class AutoZero(Enum):
    AUTO = -1
    '''
    The drivers chooses the AutoZero setting based on the configured method  and resolution.
    '''
    OFF = 0
    '''
    Disables AutoZero.
    '''
    ON = 1
    '''
    The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.
    '''
    ONCE = 2
    '''
    The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.
    '''


class CableCompensationType(Enum):
    NONE = 0
    '''
    No Cable Compensation
    '''
    OPEN = 1
    '''
    Open Cable Compensation
    '''
    SHORT = 2
    '''
    Short Cable Compensation
    '''
    OPEN_AND_SHORT = 3
    '''
    Open and Short Cable Compensation
    '''


class DCNoiseRejection(Enum):
    AUTO = -1
    '''
    The driver chooses the DC noise rejection setting based on the configured  method and resolution.
    '''
    NORMAL = 0
    '''
    NI-DMM weighs all samples equally.
    '''
    SECOND_ORDER = 1
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing method.
    '''
    HIGH_ORDER = 2
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing method.
    '''


class Function(Enum):
    DC_VOLTS = 1
    '''
    DC Voltage
    '''
    AC_VOLTS = 2
    '''
    AC Voltage
    '''
    DC_CURRENT = 3
    '''
    DC Current
    '''
    AC_CURRENT = 4
    '''
    AC Current
    '''
    _2_WIRE_RES = 5
    '''
    2-Wire Resistance
    '''
    _4_WIRE_RES = 101
    '''
    4-Wire Resistance
    '''
    FREQ = 104
    '''
    Frequency
    '''
    PERIOD = 105
    '''
    Period
    '''
    TEMPERATURE = 108
    '''
    NI 4065, and NI 4070/4071/4072 supported.
    '''
    AC_VOLTS_DC_COUPLED = 1001
    '''
    AC Voltage with DC Coupling
    '''
    DIODE = 1002
    '''
    Diode
    '''
    WAVEFORM_VOLTAGE = 1003
    '''
    Waveform voltage
    '''
    WAVEFORM_CURRENT = 1004
    '''
    Waveform current
    '''
    CAPACITANCE = 1005
    '''
    Capacitance
    '''
    INDUCTANCE = 1006
    '''
    Inductance
    '''


class LCCalculationModel(Enum):
    AUTO = -1
    '''
    NI-DMM chooses the algorithm based on method and range
    '''
    SERIES = 0
    '''
    NI-DMM uses the series impedance model to calculate capacitance and inductance
    '''
    PARALLEL = 1
    '''
    NI-DMM uses the parallel admittance model to calculate capacitance and inductance
    '''


class MeasurementCompleteDest(Enum):
    NONE = -1
    '''
    No Trigger
    '''
    EXTERNAL = 2
    '''
    AUX I/O Connector
    '''
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    LBR_TRIG0 = 1003
    '''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class MeasurementDestinationSlope(Enum):
    POSITIVE = 0
    '''
    Rising Edgs
    '''
    NEGATIVE = 1
    '''
    Falling Edge
    '''


class OperationMode(Enum):
    IVIDMM = 0
    '''
    IviDmm Mode
    '''
    WAVEFORM = 1
    '''
    Waveform acquisition mode
    '''


class RTDType(Enum):
    CUSTOM = 0
    '''
    Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
    and C coefficients.
    '''
    PT3750 = 1
    '''
    Performs scaling for a Pt 3750 RTD.
    '''
    PT3851 = 2
    '''
    Performs scaling for a Pt 3851 RTD.
    '''
    PT3911 = 3
    '''
    Performs scaling for a Pt 3911 RTD.
    '''
    PT3916 = 4
    '''
    Performs scaling for a Pt 3916 RTD.
    '''
    PT3920 = 5
    '''
    Performs scaling for a Pt 3920 RTD.
    '''
    PT3928 = 6
    '''
    Performs scaling for a Pt 3928 RTD.
    '''


class SampleTrigSlope(Enum):
    POSITIVE = 0
    '''
    Rising Edgs
    '''
    NEGATIVE = 1
    '''
    Falling Edge
    '''


class SampleTrigger(Enum):
    IMMEDIATE = 1
    '''
    No Trigger
    '''
    EXTERNAL = 2
    '''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    '''
    Software Trigger
    '''
    INTERVAL = 10
    '''
    Interval Trigger
    '''
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    '''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    '''
    AUX I/0 Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    '''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class ThermistorType(Enum):
    CUSTOM = 0
    '''
    Custom
    '''
    _44004 = 1
    '''
    44004
    '''
    _44006 = 2
    '''
    44006
    '''
    _44007 = 3
    '''
    44007
    '''


class ThermocoupleReferenceJunctionType(Enum):
    FIXED = 2
    '''
    Thermocouple reference juction is fixed at the user-specified
    temperature.
    '''


class ThermocoupleType(Enum):
    B = 1
    '''
    Thermocouple type B
    '''
    E = 4
    '''
    Thermocouple type E
    '''
    J = 6
    '''
    Thermocouple type J
    '''
    K = 7
    '''
    Thermocouple type K
    '''
    N = 8
    '''
    Thermocouple type N
    '''
    R = 9
    '''
    Thermocouple type R
    '''
    S = 10
    '''
    Thermocouple type S
    '''
    T = 11
    '''
    Thermocouple type T
    '''


class TransducerType(Enum):
    THERMOCOUPLE = 1
    '''
    Thermocouple
    '''
    THERMISTOR = 2
    '''
    Thermistor
    '''
    _2_WIRE_RTD = 3
    '''
    2-wire RTD
    '''
    _4_WIRE_RTD = 4
    '''
    4-wire RTD
    '''


class TriggerSlope(Enum):
    POSITIVE = 0
    '''
    Rising Edgs
    '''
    NEGATIVE = 1
    '''
    Falling Edge
    '''


class TriggerSource(Enum):
    IMMEDIATE = 1
    '''
    No Trigger
    '''
    EXTERNAL = 2
    '''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    '''
    Software Trigger
    '''
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    '''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    '''
    AUX I/O Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    '''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class WaveformCoupling(Enum):
    AC = 0
    '''
    AC Coupled
    '''
    DC = 1
    '''
    DC Coupled
    '''
