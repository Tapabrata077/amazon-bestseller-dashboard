import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("📚 Amazon Best Seller Dashboard")
uploaded_file=st.file_uploader("Upload CSV",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    
    if "index" in df.columns:
        df=df.drop(columns=["index"])
        
    with st.container():
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.metric("📚 Total books",len(df))
        with col2:
            st.metric("✍️ Total Authors",df["Author"].nunique())
        with col3:
            st.metric("⭐ Average Rating",round(df["Book_average_rating"].mean(),2))
        with col4:
            st.metric("💰 Average Price",round(df["sale price"].mean(),2))
        
    with st.container():
        st.subheader("📒 Filterted Books")
        search=st.text_input("🔍 Search Book")
        
        st.sidebar.header("📌 Filters")
        author=st.sidebar.selectbox(
            "✍️ Author",
            ["All"]+sorted(df["Author"].unique().tolist())
        )
        year=st.sidebar.selectbox(
            "📅 Year",
          ["All"]+sorted(df["Publishing Year"].dropna().astype(int).unique().tolist())
        )
        genre=st.sidebar.selectbox(
            "📚 Genre",
            ["All"]+sorted(df["genre"].unique().tolist())
        )
        min_price=int(df["sale price"].min())
        max_price=int(df["sale price"].max())
        price_range=st.sidebar.slider(
            "💰 Price Range",
            min_value=min_price,
            max_value=max_price,
            value=(min_price,max_price)
        )
        f_df=df.copy()
        if search:
            f_df=f_df[f_df["Book Name"].str.contains(search,case=False,na=False)]
        if author != "All":
            f_df=f_df[f_df["Author"]==author]
        if year != "All":
            f_df=f_df[f_df["Publishing Year"]==year]
        if genre != "All":
            f_df=f_df[f_df["genre"]==genre]
        f_df=f_df[
            (f_df["sale price"]>=price_range[0]) &
            (f_df["sale price"]<=price_range[1])
        ]
        st.success(f"Showing {len(f_df)} of {len(df)} books")
        st.dataframe(f_df)
    
#DOWNLOAD

        csv=f_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered CSV",
            data=csv,
            file_name="filtered_books.csv",
            mime="text/csv"
        )
        st.divider()
        
    with st.container():
        
        st.subheader("📊 Charts")
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Top 10 Authors")
            top_authors=f_df["Author"].value_counts().head(10)
            fig1,ax=plt.subplots(figsize=(10,5))
            top_authors.plot(kind="bar",ax=ax)
            ax.set_title("Top 10 authors")
            ax.set_xlabel("Author")
            ax.set_ylabel("Number of books")
            st.pyplot(fig1)

        with col2:
            st.subheader("📚 Genre Distribution")
            genre_count=f_df["genre"].value_counts()
            fig2,ax=plt.subplots()
            ax.pie(
                genre_count,
                labels=genre_count.index,
                autopct="%1.1f%%"
            )
            ax.set_title("Genre Distribution")
            st.pyplot(fig2)

        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader("📅 Books Published Per Year")
            year_count=f_df["Publishing Year"].value_counts().sort_index()
            fig3,ax=plt.subplots(figsize=(12,5))
            ax.plot(year_count.index,year_count.values,marker='o')
            ax.set_xlabel("year")
            ax.set_ylabel("books")
            st.pyplot(fig3)
            
        with col4:
            st.subheader("💰 Price Distribution")
            fig4,ax=plt.subplots()
            ax.hist(f_df["sale price"],bins=10)
            ax.set_xlabel("Price")
            ax.set_ylabel("Frequency")
            st.pyplot(fig4)

        col5 = st.columns(1)[0]
        
        with col5:
            st.subheader("⭐️ Rating Distribution")
            fig,ax=plt.subplots(figsize=(10,6))
            ax.scatter(
                f_df["Book_ratings_count"],
                f_df["Book_average_rating"],
                alpha=0.6
            )
            ax.set_ylabel("Average Rating")
            ax.set_xlabel("Rating Count")
            ax.set_title("Average Rating vs Rating Count")
            st.pyplot(fig)
    
    