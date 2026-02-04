# Mersenne-52
More information about prime numbers and Mersenne 52 at https://www.mersenne.org/primes/press/M136279841.html
More information about Mersenne 52 at https://t5k.org/largest.html#references

Prime numbers are numbers that can be divided by only 2 numbers, 1 and itself. 
(I.e. 1, 2, 3, 5, 7, 11, 13, …)

The largest know prime number is known as “Mersenne 52?” according to t5k.org.
Mersenne 52 is 41,024,320 digits long and so it is crucial to be careful with this script.
I ran this Python script on my M4 Pro MacBook Pro which has 
* 24 GB unified memory, 
* 512 GB SSD storage,
* M4 Pro 14-core CPU,
* M4 Pro 20-core GPU,
* M4 Pro 16-core Neural Engine.
I was running macOS Tahoe 26.2 (25C56) and version Python 3.13.2 .

This is just my setup and I was tracking macOS Activity Monitor concurrently, observing the highest memory usage of 20 GB and highest CPU of 19.91%. My computer was plugged into charge and was at 100% battery.

This script is memory heavy and so I would recommend 32 GB of unified memory to protect your machine.


The following is my reflection and iterations that I made before getting this final version.

I was curious about math research and advancements in modern day (2024 - 2025). I meant to search “latest mathematical discoveries” on google, but I accidentally prompted AI mode powered by Google Gemini. Under a “Major Breakthroughs” section, there were four advancements, the last of which was “New Larges Prime Number” with a description of it. I was intrigued by the number of digits and I wanted to see what the number was. I opened GPT-5 Mini by OpenAI and prompted, “What is the largest known prime number. Please list out all of the digits.” Expectedly, ChatGPT declined and told me two things. First, the largest known prime number is over 41 million digits and cannot be displayed in the application. Second, large prime numbers are in Mersenne Prime Form which uses the equation “2^p ± 1”. I focused on the first teaching in this project.

Since ChatGPT could not display the largest known prime, I took matters into my own hands to fulfill my curiosity. Using t5k.org, I found that Mersenne 52 is represented as “(2^136279841) - 1”. I opened Visual Studio Code and created a variable that had a value of “(2^136279841) - 1”, also known as Mersenne 52. Then, I simply printed this variable only to run into a syntax error. Python can only convert 4300 integers to a string, which is significantly shorter than Mersenne 52. To fix this, I changed that limit to 41024321 using sys.set, but I quickly ran into another syntax error. This took me a couple seconds to realize that I needed to import sys before using sys.set; simple fix. Then, to test if the conversion limit had changed, I printed the new limit. At this point, the script ran well, but to make the output easier to understand, I printed when Mersenne 52 starts and when it ends. Finally, to make sure that the result was accurate, I tested its length by converting the variable to a string and then using len(). In total, this program was written in eight lines.

My future plan is to tweak this program so that it can take input for any prime number in Mersenne Prime Form and output the value of it. This will be helpful to people who want to see the largest known primes and as more research is done, this script will still be able to display a result. Issues that I expect include the maximum integer to string conversion rate being too low and making a comfortable user interface that asks for the p value (from 2^p ± 1) and whether 1 needs to be added or subtracted.
