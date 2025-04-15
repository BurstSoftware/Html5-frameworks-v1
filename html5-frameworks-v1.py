import streamlit as st

# Data structure for HTML5 frameworks categorized
frameworks_data = {
    "Front-End HTML5 Frameworks": {
        "Bootstrap": "Popular framework with HTML5, CSS, and JS for responsive, mobile-first websites.",
        "Foundation": "Modern, responsive framework with a mobile-first approach.",
        "HTML5 Boilerplate": "Lean starting template for fast, modern websites.",
        "Semantic UI": "Uses human-friendly HTML5 syntax for responsive interfaces.",
        "UIkit": "Lightweight, modular framework for fast web interfaces.",
        "Skeleton": "Simple, lightweight CSS boilerplate for small projects.",
        "MontageJS": "Framework for modern SPAs with data-UI synchronization.",
        "SproutCore": "MVC-based framework for native-like web experiences.",
        "Pure.css": "Small set of CSS modules for lightweight, responsive designs.",
        "Milligram": "Minimalist CSS framework with a tiny footprint."
    },
    "JavaScript-Driven HTML5 Frameworks": {
        "CreateJS": "Suite of JS libraries for rich, interactive HTML5 content.",
        "LimeJS": "HTML5 game framework optimized for touch screens.",
        "Phaser": "Popular framework for creating 2D HTML5 games.",
        "Babylon.js": "Powerful framework for 3D games using WebGL.",
        "Zino UI": "jQuery-based framework with a rich widget library."
    },
    "Full-Stack or Hybrid HTML5 Frameworks": {
        "Meteor": "Full-stack JS framework for rapid web/mobile apps.",
        "Monaca": "Cloud-based framework for cross-platform mobile apps."
    },
    "Specialized HTML5 Frameworks": {
        "Less Framework": "Minimalist framework with pre-built responsive layouts.",
        "Bojler": "Framework for creating responsive email templates.",
        "NES.css": "Retro-styled framework mimicking NES aesthetics."
    }
}

# Streamlit app
def main():
    # Title of the app
    st.title("HTML5 Frameworks Explorer")

    # Dropdown menu at the top of the main app
    category = st.selectbox(
        "Select a Framework Category",
        options=list(frameworks_data.keys()),
        index=0  # Default to the first category
    )

    # Display the selected category's frameworks
    st.subheader(f"Frameworks in {category}")
    frameworks = frameworks_data[category]
    
    # Display each framework and its description in a clean list format
    for framework, description in frameworks.items():
        st.write(f"**{framework}**: {description}")

if __name__ == "__main__":
    main()
