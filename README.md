# CSV to Sankey
This Python CLI application converts a CSV into a file for [SankeyMATIC](https://sankeymatic.com) to create Sankey diagrams. 

⚠️ Still a work in progress

![Sankey diagram](https://i.imgur.com/6xD6dXu.png)

## How to use
1. Create a spreadsheet with Excel, Libre Calc, Numbers, Google Sheet, or other. 
2. Ensure your CSV has the following columns: Source, Target, and Volume. Source and Target corresponds to labels and where the Sankey flows from and to. Volume is the amount flowing from the source to the target.
4. Export as CSV
5. Run `ctskey -f <path-to-csv-file>`
6. Open the `out` directory and view the contents of `sankey.skmt`.

## Next step
Currently this program will only create a file which you then must copy and paste into SankeyMATIC. My plan is to write a web scraper which will interact with the form on the site and return the user a Sankey diagram.
