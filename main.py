import streamlit as st
from scrape import scrapefish_website, build_js_scenario
from parse import parse_large_content
from ui_config import configure_pagination
from utils.calculate_cost import calculate_token_cost

# Set page layout
st.set_page_config(
    page_title="Web Scraper Configuration",
    layout="wide",
)

def main():
    # ==========================
    # Sidebar UI
    # ==========================
    st.sidebar.title("Configuration Options")
    pagination_config = configure_pagination()

    # ==========================
    # Main content area
    # ==========================
    st.title("Web Scraper Tool")
    website_url = st.text_input("Enter the URL of the website to scrape")
    question = st.text_area(
        "Describe the information you want to extract (e.g., 'Collect all of the relevant property information, etc.')"
    )

    if st.button("Scrape"):
        if not website_url:
            st.error("Please enter a valid URL!")
            return
        elif not question:
            st.error("Please provide a question or instructions!")
            return

        with st.spinner("Scraping and parsing in progress... Please wait."):
            try:
                # 1) Build scenario based on user config
                scenario = build_js_scenario(
                    pagination_type=pagination_config["pagination_type"],
                    num_scrolls=pagination_config["num_scrolls"],
                    scroll_pixels=pagination_config["scroll_pixels"],
                    num_button_clicks=pagination_config["num_button_clicks"],
                    button_selector=pagination_config["button_selector"]
                )

                # 2) Scrape using that scenario
                context = scrapefish_website(website_url, scenario)

                # 3) Parse
                results = parse_large_content(context, question)

                # 4) Calculate cost
                prompt_tokens = results["total_prompt_tokens"]
                completion_tokens = results["total_completion_tokens"]
                total_cost = calculate_token_cost(
                    model_name="gpt-3.5-turbo",
                    prompt_tokens=prompt_tokens,
                    completion_tokens=completion_tokens
                )

                # 5) Show results
                if results and results["merged_records"]:
                    st.success("Parsing completed successfully!")
                    st.json(results["merged_records"])

                    st.info(f"""
                    **Token Usage:**
                    - Prompt Tokens: {prompt_tokens}
                    - Completion Tokens: {completion_tokens}
                    - Total Tokens: {results['total_tokens']}

                    **Estimated Cost:** ${total_cost:.6f}
                    """)
                else:
                    st.warning("No data matched the provided question.")

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
