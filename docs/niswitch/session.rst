niswitch.Session
================

.. py:module:: niswitch

.. py:class:: Session

   An NI-SWITCH session to a National Instruments Switch Module

   **Properties**

   +------------------------------------------------------+----------------------------------+
   | Property                                             | Datatype                         |
   +======================================================+==================================+
   | :py:attr:`analog_bus_sharing_enable`                 | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`bandwidth`                                 | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`cabled_module_scan_advanced_bus`           | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`cabled_module_trigger_bus`                 | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`cache`                                     | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`channel_count`                             | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`characteristic_impedance`                  | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`continuous_scan`                           | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`digital_filter_enable`                     | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`driver_setup`                              | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`group_capabilities`                        | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`handshaking_initiation`                    | :py:data:`HandshakingInitiation` |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`instrument_firmware_revision`              | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`instrument_manufacturer`                   | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`instrument_model`                          | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`interchange_check`                         | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`io_resource_descriptor`                    | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`is_configuration_channel`                  | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`is_debounced`                              | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`is_scanning`                               | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`is_source_channel`                         | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`is_waiting_for_trig`                       | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`logical_name`                              | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`master_slave_scan_advanced_bus`            | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`master_slave_trigger_bus`                  | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_ac_voltage`                            | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_carry_ac_current`                      | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_carry_ac_power`                        | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_carry_dc_current`                      | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_carry_dc_power`                        | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_dc_voltage`                            | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_switching_ac_current`                  | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_switching_ac_power`                    | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_switching_dc_current`                  | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`max_switching_dc_power`                    | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`number_of_relays`                          | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`num_of_columns`                            | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`num_of_rows`                               | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`parsed_scan_list`                          | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`power_down_latching_relays_after_debounce` | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`range_check`                               | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`record_coercions`                          | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`scan_advanced_output`                      | :py:data:`ScanAdvancedOutput`    |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`scan_advanced_polarity`                    | :py:data:`ScanAdvancedPolarity`  |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`scan_delay`                                | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`scan_list`                                 | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`scan_mode`                                 | :py:data:`ScanMode`              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`serial_number`                             | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`settling_time`                             | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`simulate`                                  | bool                             |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`specific_driver_class_spec_major_version`  | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`specific_driver_class_spec_minor_version`  | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`specific_driver_description`               | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`specific_driver_revision`                  | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`specific_driver_vendor`                    | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`supported_instrument_models`               | str                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`temperature`                               | float                            |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`trigger_input`                             | :py:data:`TriggerInput`          |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`trigger_input_polarity`                    | :py:data:`TriggerInputPolarity`  |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`trigger_mode`                              | int                              |
   +------------------------------------------------------+----------------------------------+
   | :py:attr:`wire_mode`                                 | int                              |
   +------------------------------------------------------+----------------------------------+

   **Public methods**

   +---------------------------------------+
   | Method name                           |
   +=======================================+
   | :py:func:`abort`                      |
   +---------------------------------------+
   | :py:func:`can_connect`                |
   +---------------------------------------+
   | :py:func:`commit`                     |
   +---------------------------------------+
   | :py:func:`configure_scan_list`        |
   +---------------------------------------+
   | :py:func:`configure_scan_trigger`     |
   +---------------------------------------+
   | :py:func:`connect`                    |
   +---------------------------------------+
   | :py:func:`connect_multiple`           |
   +---------------------------------------+
   | :py:func:`disable`                    |
   +---------------------------------------+
   | :py:func:`disconnect`                 |
   +---------------------------------------+
   | :py:func:`disconnect_all`             |
   +---------------------------------------+
   | :py:func:`disconnect_multiple`        |
   +---------------------------------------+
   | :py:func:`get_channel_name`           |
   +---------------------------------------+
   | :py:func:`get_path`                   |
   +---------------------------------------+
   | :py:func:`get_relay_count`            |
   +---------------------------------------+
   | :py:func:`get_relay_name`             |
   +---------------------------------------+
   | :py:func:`get_relay_position`         |
   +---------------------------------------+
   | :py:func:`relay_control`              |
   +---------------------------------------+
   | :py:func:`reset`                      |
   +---------------------------------------+
   | :py:func:`reset_with_defaults`        |
   +---------------------------------------+
   | :py:func:`route_scan_advanced_output` |
   +---------------------------------------+
   | :py:func:`route_trigger_input`        |
   +---------------------------------------+
   | :py:func:`self_test`                  |
   +---------------------------------------+
   | :py:func:`send_software_trigger`      |
   +---------------------------------------+
   | :py:func:`set_continuous_scan`        |
   +---------------------------------------+
   | :py:func:`set_path`                   |
   +---------------------------------------+
   | :py:func:`wait_for_debounce`          |
   +---------------------------------------+
   | :py:func:`wait_for_scan_complete`     |
   +---------------------------------------+


