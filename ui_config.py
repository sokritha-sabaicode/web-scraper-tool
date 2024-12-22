import streamlit as st

def configure_pagination():
    """
    Draws pagination settings in the Streamlit sidebar
    and returns the user's choices.

    Currently supports:
      - No pagination ("None")
      - Infinite scroll pagination ("Scroll")
      - Button-based pagination ("Button")
    """
    st.sidebar.subheader(
        "Pagination Options",
        help=(
            "Select how the target website loads additional content.\n\n"
            "• 'None' means no extra pagination steps.\n"
            "• 'Scroll' means the site loads new data on scrolling.\n"
            "• 'Button' means the site requires a 'Load More' or 'Next' button click.\n"
        )
    )

    pagination_type = st.sidebar.selectbox(
        "Select pagination type:",
        options=["None", "Scroll", "Button"],
        index=0
    )

    # Defaults
    num_scrolls = 1
    scroll_pixels = 1400
    num_button_clicks = 1
    button_selector = "#load-more"

    if pagination_type == "Scroll":
        st.sidebar.markdown(
            "If your site loads more data automatically as you scroll down, configure below."
        )
        num_scrolls = st.sidebar.number_input(
            "How many times to scroll?",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
        )
        scroll_pixels = st.sidebar.number_input(
            "Scroll distance (pixels) per step?",
            min_value=100,
            max_value=10000,
            value=1400,
            step=100,
            help="How far down to scroll each time."
        )

    elif pagination_type == "Button":
        st.sidebar.markdown(
            "If your site loads more items on a 'Load More' or 'Next Page' button click, configure below."
        )
        num_button_clicks = st.sidebar.number_input(
            "Number of button clicks",
            min_value=1,
            max_value=50,
            value=3,
            step=1,
            help="How many times to click the button to load more data."
        )
        button_selector = st.sidebar.text_input(
            "CSS Selector for 'Load More' or 'Next' button",
            value="#load-more",
            help="Provide a valid selector for the button you need to click (e.g. '#load-more')."
        )

    return {
        "pagination_type": pagination_type,    # "None", "Scroll", or "Button"
        "num_scrolls": num_scrolls,
        "scroll_pixels": scroll_pixels,
        "num_button_clicks": num_button_clicks,
        "button_selector": button_selector
    }
