# Course 1
-

# Course 2
### chaining.ipynb
#### Forward Chaining
1. assume that the name of object is **name** variable.
2. declare 2 variables what can object do for the rules in this case **what_can_do_1** and **what_can_do_2**.
3. in **data_source_object_identify** is the data of rules which will produce conclusions from 2 variables in number 2 (ex. A & B => C).
4.  **data_colour_by_object_identifier** contains colour data by the object identify from result number 3 (ex. C => D).
5. then loop at **data_source_object_identify** and if **what_can_do_1** in identifier 1 or 2 and **what_can_do_2** in identifier 1 or identifier 2 it will save the result to **object_identifier**.
6. after get the result what object is, loop at **data_colour_by_object_identifier** to get what is the colour from the object identifier and save to **what_is_the_color_of** variable.

#### Backward Chaining
1. for backward chaining all variables is same, the difference is only the process for getting conclusions.
2. now loop from **data_colour_by_object_identifier** first, and get what the object is.
3. now do nested loops inside **data_colour_by_object_identifier** loops, and find where is the object from **data_source_object_identify** rules/data
4. then if **what_can_do_1** in identifier 1 or 2 and **what_can_do_2** in identifier 1 or identifier 2 it will get the colour and save the colour to **what_is_the_color_of** variable.
