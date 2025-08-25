#!/usr/local/bin/python3
#
# 重新创建 README.md 文件
#

lastWeekDate = open('week/last.date').read()
lastWeekRank = open("week/%s.md"%(lastWeekDate), 'r').read()
lastMonthDate = open('month/last.date').read()
lastMonthRank = open("month/%s.md"%(lastMonthDate), 'r').read()

datas = {
    '{last-week-date}': lastWeekDate,
    '{last-week-rank}': lastWeekRank,
    '{last-month-date}': lastMonthDate,    
    '{last-month-rank}': lastMonthRank
    }

with open('README.md.model', 'r') as f:
    md = f.read()
    for key in datas:
        md = md.replace(key, datas[key])
    
    with open('README.md', 'w') as w:
        w.write(md)