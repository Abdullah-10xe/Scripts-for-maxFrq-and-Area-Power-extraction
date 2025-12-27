import csv
import re
import sys


def timing_finding():
    timing_text = open("/home/abdullah/logic_synthesis_project/scripts/reports/report_timing.rpt", 'r')
    timing_text = timing_text.read()
    clock = re.search("Clock\s*Edge:\+\s*([\d]+\.?[\d]*)", timing_text)
    slack = re.search("Slack:=\s*(-?[\d]+\.?[\d]*)", timing_text)
    return [(clock.group(1)), slack.group(1)]


timing_data = timing_finding()


def area_finding():
    area_text = open("/home/abdullah/logic_synthesis_project/scripts/reports/report_area.rpt", "r")
    area_text = area_text.read()
    area = re.findall(
        "MSpVM\s*[\d]*\.?[\d]?\s*[\d]*\.?[\d]*\s*[\d]*\.?[\d]*\s*([\d]*\.?[\d]*)\s*[\d]*\.?[\d]*\s*[\d]*\.[\d]*\s*([\d]*\.?[\d]*)", area_text)
    combinational_area = area[0][0]
    non_combinational_area = area[0][1]
    return [combinational_area, non_combinational_area]


area_data = area_finding()


def power_findings():

    power_text = open("/home/abdullah/logic_synthesis_project/scripts/reports/report_power.rpt", 'r')
    power_text = power_text.read()
    power = re.search(
        "Subtotal\s*([\d]*\.?[\d]*e?-?[\d]*)\s*([\d]*\.?[\d]*e?-?[\d]*)\s*([\d]*\.?[\d]*e?-?[\d]*)", power_text)
    static_power = power.group(1)
    dynamic_power = float(power.group(2))+float(power.group(3))
    return [static_power, dynamic_power]


power_data = power_findings()

rows = [[" PPA DATA", " ", " ", "Area", " ", " ", "Power", " ", " ", " Timing "],
        [" ", " ", " ", "  Combinational Area   ", "Non_Combinational Area",
            " ", "Static Power", " dynamic power", " ", "Slack ", "Period "],
        ["", " ", " ", f'{area_data[0]}', f'{area_data[1]}', " ", f'{power_data[0]}',
         f'{ power_data[1]}', " ", f'{ timing_data[1]}', f'{timing_data[0]}']






        ]

append = ["", " ", " ", f'{area_data[0]}', f'{area_data[1]}', " ", f'{power_data[0]}',
          f'{ power_data[1]}', " ", f'{ timing_data[1]}', f'{timing_data[0]}']
if sys.argv[1] == '0':
    with open("result1.csv", 'w') as file:
        writer = csv.writer(file)
        for i in rows:
            writer.writerow(i)

else:
    with open("result1.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(append)
        
print(timing_data[1])

