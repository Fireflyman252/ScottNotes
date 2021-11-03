ScottNotes is a program to maintain a daily Todo list.  The basic idea is that an item can be added to the list and will stay on the list until it is marked complete.  Completed items will be removed the next day when the day is updated (File→Update Today).  Also future items or appointment can be set in the “Calendar” function.

ScottNotes uses QT for the GUI elements.  GUI elements are created using QT Designer 5 and converted to python.  The “.ui” file is the QT Designer 5 file and the same named “.py” file is generated file.

I then added the ability to extract the daily events from a google calendar, since my wife kept the schedule for the kids in a google calendar.  So the “Update Today” action will extract today’s calendar events as well as several google calendars that my wife maintains.

In addition to the “Today” tab, ScottNotes has the ability to maintain several tabs, each of which has the basic list capability of adding, removing and updating items.
