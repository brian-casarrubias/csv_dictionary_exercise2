
'''
date,temperature(F)
Jan 1,27
Jan 2,31
Jan 3,23
Jan 4,34
Jan 5,37
Jan 6,38
Jan 7,29
Jan 8,30
Jan 9,35
Jan 10,30


a. What was the temperature on Jan 9?
b. What was the temperature on Jan 4?

* opened the csv file in read mode, made an empty dictionary to store the values and be able to access the values that I will add on later quicly and efficienlty
* with the 'next(file_reader)' I skipped the header because we dont need it in this case
* used a for loop to iterate
*set the weathger_dict key to be the current date, and the value to be the current temperature
*once its done iterating, and all the values are inside the dictionary, we are all done
*we can now easily just search up lets say 'jan 9' and it will give us the value/temperature of that day!