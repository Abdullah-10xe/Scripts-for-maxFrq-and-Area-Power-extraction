
set t [lindex $argv 0]
set duty [expr {1.0*$t/2}]
puts $t
set_db init_lib_search_path ../12_nm_lib/
set_db init_hdl_search_path ../rtl/
read_libs  tcbn12ffcllbwp16p90ssgnp0p9v125c_ccs.lib
read_hdl -sv {control_logic.sv fifo.sv input_memories.sv mac_pipe.sv}
elaborate
create_clock -name clk -period   $t    -waveform [list 0 $duty] [get_ports "clk"]
read_sdc /home/abdullah/logic_synthesis_project/sdc_files/constraint.sdc
set_db syn_generic_effort medium
set_db syn_map_effort medium
set_db syn_opt_effort medium

syn_generic
syn_map
syn_opt

#reports
report_timing > reports/report_timing.rpt
report_power  > reports/report_power.rpt
report_area -detail  > reports/report_area.rpt
report_qor    > reports/report_qor.rpt



#Outputs
write_hdl > outputs/MX_netlist.v
write_sdc > outputs/MX_sdc.sdc
write_sdf -timescale ns -nonegchecks -recrem split -edges check_edge  -setuphold split > outputs/delays.sdf 

exit

