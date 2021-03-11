# Gwyddion_AFM_profiles_batch
Calculate 2D material height difference (i.e. thickness) from exported CSV file of selected profiles from Gwyddion.

The thickenss is calculate from the difference of the z-axis (height) of the 1st and the last point in the line profile selected. i.e.:

thickness=|Z<sub>1</sub>-Z<sub>last</sub>|

Supported data format when export from Gwyddion as follow:

![image](https://user-images.githubusercontent.com/66976281/110798594-3c086d80-8272-11eb-941c-412dec550041.png)

By default, the result will be merged into a 'AFM merge statistics.txt' under the same dir as the data.

Good Luck!
