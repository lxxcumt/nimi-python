Enums
=====

Enums used in NI-SCOPE

.. py:currentmodule:: niscope



.. py:data:: AcquisitionType

    .. py:attribute:: niscope.AcquisitionType.NORMAL



        Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.

        



    .. py:attribute:: niscope.AcquisitionType.FLEXRES



        Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.

        



    .. py:attribute:: niscope.AcquisitionType.DDC



        Sets the digitizer to DDC mode on the NI 5620/5621.

        




.. py:data:: BoolEnableDisableChan

    .. py:attribute:: niscope.BoolEnableDisableChan.DISABLED



        Does not acquire a waveform for the channel.

        



    .. py:attribute:: niscope.BoolEnableDisableChan.ENABLED



        Acquires a waveform for the channel.

        




.. py:data:: BoolEnableDisableIQ

    .. py:attribute:: niscope.BoolEnableDisableIQ.DISABLED



        A scalar fetch returns an array of waveforms in the following format:
        III...QQQ...

        



    .. py:attribute:: niscope.BoolEnableDisableIQ.ENABLED



        (Default) A scalar fetch returns an array of waveforms in the following
        format: IQIQIQ...

        




.. py:data:: BoolEnableDisableRealtime

    .. py:attribute:: niscope.BoolEnableDisableRealtime.DISABLED



        Allow both real-time and equivalent-time measurements.

        



    .. py:attribute:: niscope.BoolEnableDisableRealtime.ENABLED



        Allow only real-time measurements.

        




.. py:data:: BoolEnableDisableTIS

    .. py:attribute:: niscope.BoolEnableDisableTIS.DISABLED



        (Default) Use only this channel's ADC to acquire data for this channel.

        



    .. py:attribute:: niscope.BoolEnableDisableTIS.ENABLED



        Use multiple interleaved ADCs to acquire data for this channel.

        




.. py:data:: DataProcessingMode

    .. py:attribute:: niscope.DataProcessingMode.REAL



        The waveform data points are real numbers (I data).

        



    .. py:attribute:: niscope.DataProcessingMode.COMPLEX



        The waveform data points are complex numbers (IQ data).

        




.. py:data:: FIRFilterWindow

    .. py:attribute:: niscope.FIRFilterWindow.NONE



        No window.

        



    .. py:attribute:: niscope.FIRFilterWindow.HANNING



        Specifies a Hanning window.

        



    .. py:attribute:: niscope.FIRFilterWindow.FLAT_TOP



        Specifies a Flat Top window.

        



    .. py:attribute:: niscope.FIRFilterWindow.HAMMING



        Specifies a Hamming window.

        



    .. py:attribute:: niscope.FIRFilterWindow.TRIANGLE



        Specifies a Triangle window.

        



    .. py:attribute:: niscope.FIRFilterWindow.BLACKMAN



        Specifies a Blackman window.

        




.. py:data:: FetchRelativeTo

    .. py:attribute:: niscope.FetchRelativeTo.READ_POINTER



        The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.

        



    .. py:attribute:: niscope.FetchRelativeTo.PRETRIGGER



        Fetches relative to the first pretrigger point requested with niScope_ConfigureHorizontalTiming.

        



    .. py:attribute:: niscope.FetchRelativeTo.NOW



        Fetch data at the last sample acquired.

        



    .. py:attribute:: niscope.FetchRelativeTo.START



        Fetch data starting at the first point sampled by the digitizer.

        



    .. py:attribute:: niscope.FetchRelativeTo.TRIGGER



        Fetch at the first posttrigger sample.

        




.. py:data:: FilterType

    .. py:attribute:: niscope.FilterType.LOWPASS



        Specifies lowpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.HIGHPASS



        Specifies highpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.BANDPASS



        Specifies bandpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.BANDSTOP



        Specifies bandstop as the filter type.

        




.. py:data:: FlexFIRAntialiasFilterType

    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._48_TAP_STANDARD



        This filter is optimized for alias protection and frequency-domain flatness

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._48_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._16_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._8_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR

        




.. py:data:: OverflowErrorReporting

    .. py:attribute:: niscope.OverflowErrorReporting.ERROR



        Execution stops and NI-SCOPE returns an error when an overflow has
        occurred in the OSP block.

        



    .. py:attribute:: niscope.OverflowErrorReporting.WARNING



        Execution continues and NI-SCOPE returns a warning when an overflow has
        occurred in the OSP block.

        



    .. py:attribute:: niscope.OverflowErrorReporting.DISABLED



        NI-SCOPE does not return an error when an overflow has occurred in the
        OSP block.

        




.. py:data:: PercentageMethod

    .. py:attribute:: niscope.PercentageMethod.LOWHIGH



        Specifies that the reference level percentages should be computed using
        the low/high method,

        



    .. py:attribute:: niscope.PercentageMethod.MINMAX



        Reference level percentages are computed using the min/max method.

        



    .. py:attribute:: niscope.PercentageMethod.BASETOP



        Reference level percentages are computed using the base/top method.

        




.. py:data:: RISMethod

    .. py:attribute:: niscope.RISMethod.EXACT_NUM_AVERAGES



        Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch function if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch function again to allow more time for the acquisition to finish.

        



    .. py:attribute:: niscope.RISMethod.MIN_NUM_AVERAGES



        Each RIS sample is the average of a least a minimum number of randomly
        distributed points.

        



    .. py:attribute:: niscope.RISMethod.INCOMPLETE



        Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch function if the RIS acquisition did not finish.  The acquisition aborts when data is returned.

        



    .. py:attribute:: niscope.RISMethod.LIMITED_BIN_WIDTH



        Limits the waveforms in the various bins to be within 200 ps of the center of the bin.

        




.. py:data:: RefLevelUnits

    .. py:attribute:: niscope.RefLevelUnits.VOLTS



        Specifies that the reference levels are given in units of volts.

        



    .. py:attribute:: niscope.RefLevelUnits.PERCENTAGE



        (Default) Specifies that the reference levels are given in percentage
        units.

        




.. py:data:: RefTriggerDetectorLocation

    .. py:attribute:: niscope.RefTriggerDetectorLocation.ANALOG_DETECTION_CIRCUIT



        use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.

        



    .. py:attribute:: niscope.RefTriggerDetectorLocation.DDC_OUTPUT



        use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.

        




.. py:data:: StreamingPositionType

    .. py:attribute:: niscope.StreamingPositionType.START



        Data is streamed from the start trigger.

        



    .. py:attribute:: niscope.StreamingPositionType.REFERENCE



        Data is streamed relative to the reference trigger and reference
        position.

        



    .. py:attribute:: niscope.StreamingPositionType.SYNC



        Data is streamed relative to the sync trigger and reference position.

        




.. py:data:: TerminalConfiguration

    .. py:attribute:: niscope.TerminalConfiguration.SINGLE_ENDED



        Channel is single ended

        



    .. py:attribute:: niscope.TerminalConfiguration.UNBALANCED_DIFFERENTIAL



        Channel is unbalanced differential

        



    .. py:attribute:: niscope.TerminalConfiguration.DIFFERENTIAL



        Channel is differential

        




.. py:data:: TriggerCoupling

    .. py:attribute:: niscope.TriggerCoupling.AC



        AC coupling

        



    .. py:attribute:: niscope.TriggerCoupling.DC



        DC coupling

        



    .. py:attribute:: niscope.TriggerCoupling.HF_REJECT



        Highpass filter coupling

        



    .. py:attribute:: niscope.TriggerCoupling.LF_REJECT



        Lowpass filter coupling

        



    .. py:attribute:: niscope.TriggerCoupling.AC_PLUS_HF_REJECT



        Highpass and lowpass filter coupling

        




.. py:data:: TriggerModifier

    .. py:attribute:: niscope.TriggerModifier.NO_TRIGGER_MOD



        Normal triggering.

        



    .. py:attribute:: niscope.TriggerModifier.AUTO



        Software will trigger an acquisition automatically if no trigger arrives
        after a certain amount of time.

        




.. py:data:: TriggerSlope

    .. py:attribute:: niscope.TriggerSlope.NEGATIVE



        Falling edge

        



    .. py:attribute:: niscope.TriggerSlope.POSITIVE



        Rising edge

        




.. py:data:: TriggerType

    .. py:attribute:: niscope.TriggerType.EDGE



        Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with niScope_ConfigureTriggerEdge.

        



    .. py:attribute:: niscope.TriggerType.TV



        Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with niScope_ConfigureTriggerVideo.

        



    .. py:attribute:: niscope.TriggerType.IMMEDIATE



        Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.

        



    .. py:attribute:: niscope.TriggerType.HYSTERESIS



        Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with niScope_ConfigureTriggerHysteresis.

        



    .. py:attribute:: niscope.TriggerType.DIGITAL



        Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with niScope_ConfigureTriggerDigital.

        



    .. py:attribute:: niscope.TriggerType.WINDOW



        Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with niScope_ConfigureTriggerWindow.

        



    .. py:attribute:: niscope.TriggerType.SOFTWARE



        Configures the digitizer for software triggering.  A software trigger occurs when niScope_SendSoftwareTrigger is called.

        




.. py:data:: TriggerWindowMode

    .. py:attribute:: niscope.TriggerWindowMode.ENTERING



        Trigger upon entering the window

        



    .. py:attribute:: niscope.TriggerWindowMode.LEAVING



        Trigger upon leaving the window

        




.. py:data:: VerticalCoupling

    .. py:attribute:: niscope.VerticalCoupling.AC



        AC coupling

        



    .. py:attribute:: niscope.VerticalCoupling.DC



        DC coupling

        



    .. py:attribute:: niscope.VerticalCoupling.GND



        GND coupling

        




.. py:data:: VideoPolarity

    .. py:attribute:: niscope.VideoPolarity.POSITIVE



        Specifies that the video signal has positive polarity.

        



    .. py:attribute:: niscope.VideoPolarity.NEGATIVE



        Specifies that the video signal has negative polarity.

        




.. py:data:: VideoSignalFormat

    .. py:attribute:: niscope.VideoSignalFormat.NTSC



        NTSC signal format supports line numbers from 1 to 525

        



    .. py:attribute:: niscope.VideoSignalFormat.PAL



        PAL signal format supports line numbers from 1 to 625

        



    .. py:attribute:: niscope.VideoSignalFormat.SECAM



        SECAM signal format supports line numbers from 1 to 625

        



    .. py:attribute:: niscope.VideoSignalFormat.M_PAL



        M-PAL signal format supports line numbers from 1 to 525

        



    .. py:attribute:: niscope.VideoSignalFormat._480I_59_94_FIELDS_PER_SECOND



        480 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._480I_60_FIELDS_PER_SECOND



        480 lines, interlaced, 60 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._480P_59_94_FRAMES_PER_SECOND



        480 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._480P_60_FRAMES_PER_SECOND



        480 lines, progressive,60 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._576I_50_FIELDS_PER_SECOND



        576 lines, interlaced, 50 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._576P_50_FRAMES_PER_SECOND



        576 lines, progressive, 50 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._720P_50_FRAMES_PER_SECOND



        720 lines, progressive, 50 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._720P_59_94_FRAMES_PER_SECOND



        720 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._720P_60_FRAMES_PER_SECOND



        720 lines, progressive, 60 frames per second

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I_50_FIELDS_PER_SECOND



        1,080 lines, interlaced, 50 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I_59_94_FIELDS_PER_SECOND



        1,080 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I_60_FIELDS_PER_SECOND



        1,080 lines, interlaced, 60 fields per second

        



    .. py:attribute:: niscope.VideoSignalFormat._1080P_24_FRAMES_PER_SECOND



        1,080 lines, progressive, 24 frames per second

        




.. py:data:: VideoTriggerEvent

    .. py:attribute:: niscope.VideoTriggerEvent.FIELD1



        Trigger on field 1 of the signal

        



    .. py:attribute:: niscope.VideoTriggerEvent.FIELD2



        Trigger on field 2 of the signal

        



    .. py:attribute:: niscope.VideoTriggerEvent.ANY_FIELD



        Trigger on the first field acquired

        



    .. py:attribute:: niscope.VideoTriggerEvent.ANY_LINE



        Trigger on the first line acquired

        



    .. py:attribute:: niscope.VideoTriggerEvent.LINE_NUMBER



        Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.

        

