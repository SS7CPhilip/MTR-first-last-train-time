# MTR-first-last-train-time
Get MTR train timetable

This branch optimized the line-wise search result. The first last train time which are not on specific line will be removed from the result. 

Known bug: When Line 1 terminal station is a transfer station with Line 2, the Line 2 timetable will still include trains bound for the other terminal of Line 1. 
已知的bug：按綫查詢查將軍澳綫首末車時刻時，油塘站之結果會包含觀塘綫往調景嶺方向的末班車
