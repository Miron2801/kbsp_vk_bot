cd /home/pi/kbsp_vk_bot/develop/
mkdir ../timetables/sql_backUp
sudo mysqldump timetable >  `date +../timetables/sql_backUp/Timetable_%Y.%m.%d.%H:%M:%S.sql`
