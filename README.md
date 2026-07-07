# Amazon Best Seller Analytics Dashboard

An interactive dashboard built using Python, Pandas, Matplotlib, and Streamlit to analyze Amazon Best Selling Books. Upload a CSV to explore filterable metrics, author/genre breakdowns, and price/rating distributions across 1,000+ titles.

**Live Demo:** : (https://amazon-bestseller-dashboard-ryvfamucgqdsngzr4n3dyu.streamlit.app/)

## Features
- Summary metrics: total books, unique authors, average rating, average price
- Filter by author, publishing year, genre, and price range
- Search books by title
- Download filtered results as CSV
- Visualizations: top 10 authors, genre distribution, books published per year, price distribution, rating vs. rating count

## Tech Stack
- Python
- Pandas
- Matplotlib
- Streamlit

## Setup

Clone the repo and install dependencies:

\`\`\`bash
git clone https://github.com/Tapabrata077/amazon-bestseller-dashboard.git
cd amazon-bestseller-dashboard
pip install -r requirements.txt
\`\`\`

Run the app:

\`\`\`bash
streamlit run main.py
\`\`\`

Then upload `Books_Data_Clean.csv` (included in this repo) when prompted.

## Dataset
`Books_Data_Clean.csv` — Amazon Best Selling Books dataset, 1,070 entries.
