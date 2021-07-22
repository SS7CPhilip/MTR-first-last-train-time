# MTR-first-last-train-time
Get MTR train timetable

=======
MTR official website doesn't provide multiple stations or line-wise search, so I made this to request and combine results from all stations. 
It relys on the MS Access database to show menu, look up station names, find all stations on a specific line etc. 

When doing the line-wise searching, the first last train time which are not on specific line will be removed from the result. 
已知的bug：按綫查詢查將軍澳綫首末車時刻時，油塘站之結果會包含觀塘綫往調景嶺方向的末班車。機場快綫與東涌綫無此問題，因爲兩綫共構各站的station ID并非相同。
