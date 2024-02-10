# LIHKG-Scrapping
A tool to analyze any post on LIHKG

### [Version 1.0] First Launch
A simple tool to export any post on LIHKG to csv file.
- Inputs: link of the post on LIHKG, pages 
- Data can be scrapped: floor, date, user id, comment, likes, dislikes

Current Challenges: 
- Still designing how the data on LIHKG could be analyzed.
  - idea 1: Applying LLM to summarize the post based on the likes and dislikes of the comments
  - idea 2: Visualizing the data i.e. number on comments each day, likes and dislikes of each comment
- Missing a GUI.
- Some short comments are minimized, where user needs to manually click the comment box to see the date, number of likes and dislikes. The current code could not scrape these data.
- Some comments could only be seen when the user logs in.
