## Python:
* Data preprocessing:
  * The dataset’s main issue lies in its format. The CSV reader was not able to detect the difference between new line characters for new rows and new line characters within a single tweet. Therefore, all new line characters were initially removed. The new line character used to separate a new row always lies before the timestamp, so we use regular expressions to detect the pattern of the timestamps and add a new line character before them.
  * While usual CSV readers are often able to detect the comma within the double quotes and the comma used as a delimiter, this is not the case in this dataset. To avoid complications in data processing, the delimiter was half-manually changed into a semi-colon. In this step, the dataset was double-checked manually to ensure the correctness of each data point. 
* Pseudoanonymization: Using hashlib, each username was provided with a unique code. After that, the columns containing the full name, profile URL, and profile picture were removed from the data frame. 
* Language detection: The library used was langdetect. By formulating a simple function, the language of each tweet was detected and appended into a new column: “language.” After that, the data frame was filtered to keep the tweets written in English, Italian, and French. 
## R:
* The columns consider the engagement statistics, which were transformed into numeric values. The column “engagement” calculates the sum of likes, comments, replies, retweets, and quotes.
* A column plot was drawn to compare the average engagement between three languages. It is clear that tweets written in French, on average, have the highest engagement score compared to English and Italian. 
