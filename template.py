import streamlit as st

# I have provided most of what you need for to use streamlit here and in README.md
# You can also check the streamlit docs at https://docs.streamlit.io/get-started
# Also, you can check a simple example from class:
# Page: https://simpson-dashboard-class.streamlit.app/
# GitHub Repo: https://github.com/RodrigoGrijalba/python-dashboard-class

st.set_page_config(page_title = "Tennessee’s Student Teacher Achievement Ratio (STAR) project", layout = "wide")

tab1, tab2, tab3 = st.tabs(["Original Paper", "Proposed Extention", "Extenson Results"])

with tab1:
    st.markdown("""
    ### Design description
    
    ### Data

    ### Original results
    The original results show an ols regression of the treament on the average achievement test scores. Finding an ATE around 7.
    """
    )
    st.image("output/table1.png") # uncomment this line if you would like to add an image

with tab2:

    st.markdown("""
    ### Proposed extension

    ### Justification
    Application of various methods of Double Machine Learning to enrich the results.
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image
    # table = pd.read_csv("<<path/to/table.csv>>") # load a table from csv to show it on the page
    # st.table(table) # show table


with tab3:

    st.markdown("""
    ### Extension results

    <<Your description here, in Markdown>>
    """
    )
    st.image("output/figures/dml_coefs.png") # uncomment this line if you would like to add an image

    st.image("output/figures/causal_tree.png")
