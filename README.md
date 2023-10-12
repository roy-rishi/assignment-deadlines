# assignment-deadlines
scrape data from Schoology assignments and compute the submission and deadline time delta. export a csv for further processing and visualization
 
## usage
### load data
* load all assignment tabs in the same window with nothing else. the entire window will be parsed for assignments
* `osascript get-data.applescript`
* copy standard output to a json file of your choosing
### process data
* define the json file location in the head of `deltas.py`
* `python3 deltas.py`
* copy the exported csv in `/data/data_due-sub-name-delta.csv` into the spreadsheet editor of your choosing

## dependencies
* pandas
* applescript requires macOS. for a slightly more sane approach, visit the Schoology api docs
