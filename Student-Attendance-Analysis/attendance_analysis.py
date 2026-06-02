import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("attendance.xlsx")
df["Attendance Percentage"] = (
    df["ATTENDED CLASSES"] /
    df["TOTAL C LASSES"]
) * 100
print("\nStudent Attendance Data:")
print(df)
low_attendance = df[df["Attendance Percentage"] < 75]
print("\nStudents Below 75% Attendance:")
print(low_attendance)
highest = df.loc[df["Attendance Percentage"].idxmax()]
print("\nHighest Attendance:")
print(highest)
lowest = df.loc[df["Attendance Percentage"].idxmin()]
print("\nLowest Attendance:")
print(lowest)
df.to_excel(
    "Attendance_Report.xlsx",
    index=False
)
print("\nAttendance report generated successfully!")
plt.figure(figsize=(10, 5))
plt.bar(
    df["STUDENT"],
    df["Attendance Percentage"]
)
plt.axhline(
    y=75,
    linestyle="--",
    label="Minimum Required (75%)"
)
plt.ylim(0, 100)
plt.title("Student Attendance Analysis")
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.legend()
plt.savefig("attendance_chart.png")
plt.show()