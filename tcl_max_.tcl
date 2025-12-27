set Time_period 4.0
set slack 0
set itration 0
while { $slack >=0 } {
set o [catch {exec genus  -f tcl_script.tcl  -execute "set argv {$Time_period}" } output ]
set slack [ exec python3 reports/data_processing.py $itration ]
set increment_f [expr {1/$Time_period +0.05}]
set Time_period [expr {1/$increment_f}]
puts "time period"
puts $Time_period 
set itration [ expr $itration +1]
puts "Slack "
puts $slack


}
puts " completed "
exit

