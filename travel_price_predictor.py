import streamlit as st

st.set_page_config(page_title="🚦 Jaipur Route & Transport Planner", layout="centered")

st.title("🛺 Jaipur Multi-Stop Route & Transport Planner")
st.write("Plan your route through multiple Jaipur landmarks with cost-effective transport suggestions.")

# Places with image URLs from Wikimedia Commons (free to use)
places = {
    "Hawa Mahal": "https://theheritageart.com/wp-content/uploads/2022/11/hawa-mahal.jpg",
    "Jal Mahal": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Floating_palace_Jaipur_India.jpg/1200px-Floating_palace_Jaipur_India.jpg",
    "Amber Fort": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUtsuVeYdDLHDsiBTlkohDm7Q6HMV0-rMerw&s",
    "City Palace": "https://s7ap1.scene7.com/is/image/incredibleindia/city-palace-jaipur-rajasthan-1?qlt=82&ts=1726660027704",
    "Jantar Mantar": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMSTf0wsmk1HR0wJvQcZebYMPISyPqcU3S7w&s",
    "Birla Mandir": "https://rajasthanyatra.in/blog/wp-content/uploads/2024/11/birla.webp",
    "Albert Hall Museum": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ-QnpGEpa0oN7nS9YO0rY2u1YGeXcGwB4Vw&s",
    "Nahargarh Fort": "https://s7ap1.scene7.com/is/image/incredibleindia/nahargarh-fort-jaipur-rajasthan-2-attr-hero?qlt=82&ts=1726660228692",
    "Galta Ji Temple": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFvPknhVd0OG972CGuRbZuR0u8Nz0Md0nxTQ&s",
    "Central Park Jaipur": "https://s7ap1.scene7.com/is/image/incredibleindia/central-park-jaipur-rajasthan-2-attr-hero?qlt=82&ts=1726660266223"
}

transport_options = {
    "Auto-rickshaw": 10,
    "Taxi": 15,
    "Bus": 5
}

distances = {
    ("Hawa Mahal", "Jal Mahal"): 5,
    ("Hawa Mahal", "Amber Fort"): 11,
    ("Hawa Mahal", "City Palace"): 2,
    ("Hawa Mahal", "Jantar Mantar"): 1.5,
    ("Hawa Mahal", "Birla Mandir"): 7,
    ("Hawa Mahal", "Albert Hall Museum"): 3,
    ("Hawa Mahal", "Nahargarh Fort"): 9,
    ("Hawa Mahal", "Galta Ji Temple"): 15,
    ("Hawa Mahal", "Central Park Jaipur"): 6,

    ("Jal Mahal", "Amber Fort"): 10,
    ("Jal Mahal", "City Palace"): 5,
    ("Jal Mahal", "Jantar Mantar"): 4.5,
    ("Jal Mahal", "Birla Mandir"): 6,
    ("Jal Mahal", "Albert Hall Museum"): 7,
    ("Jal Mahal", "Nahargarh Fort"): 11,
    ("Jal Mahal", "Galta Ji Temple"): 12,
    ("Jal Mahal", "Central Park Jaipur"): 9,

    ("Amber Fort", "City Palace"): 13,
    ("Amber Fort", "Jantar Mantar"): 12,
    ("Amber Fort", "Birla Mandir"): 18,
    ("Amber Fort", "Albert Hall Museum"): 14,
    ("Amber Fort", "Nahargarh Fort"): 4,
    ("Amber Fort", "Galta Ji Temple"): 16,
    ("Amber Fort", "Central Park Jaipur"): 12,

    ("City Palace", "Jantar Mantar"): 1,
    ("City Palace", "Birla Mandir"): 6,
    ("City Palace", "Albert Hall Museum"): 2,
    ("City Palace", "Nahargarh Fort"): 8,
    ("City Palace", "Galta Ji Temple"): 13,
    ("City Palace", "Central Park Jaipur"): 5,

    ("Jantar Mantar", "Birla Mandir"): 7,
    ("Jantar Mantar", "Albert Hall Museum"): 2,
    ("Jantar Mantar", "Nahargarh Fort"): 9,
    ("Jantar Mantar", "Galta Ji Temple"): 13,
    ("Jantar Mantar", "Central Park Jaipur"): 6,

    ("Birla Mandir", "Albert Hall Museum"): 7,
    ("Birla Mandir", "Nahargarh Fort"): 14,
    ("Birla Mandir", "Galta Ji Temple"): 17,
    ("Birla Mandir", "Central Park Jaipur"): 11,

    ("Albert Hall Museum", "Nahargarh Fort"): 9,
    ("Albert Hall Museum", "Galta Ji Temple"): 14,
    ("Albert Hall Museum", "Central Park Jaipur"): 4,

    ("Nahargarh Fort", "Galta Ji Temple"): 18,
    ("Nahargarh Fort", "Central Park Jaipur"): 10,

    ("Galta Ji Temple", "Central Park Jaipur"): 20
}

# Add reverse distances
all_distances = distances.copy()
for (start, end), dist in distances.items():
    if (end, start) not in all_distances:
        all_distances[(end, start)] = dist

# Select places for route
st.subheader("Select places to visit in order (at least 2):")
selected_places = st.multiselect("Choose Jaipur landmarks:", list(places.keys()))

if len(selected_places) < 2:
    st.info("Please select at least two places to form a route.")
else:
    st.markdown("### Your Selected Route:")
    st.write(" → ".join(selected_places))

    total_distance = 0
    missing_pairs = []
    for i in range(len(selected_places) - 1):
        pair = (selected_places[i], selected_places[i + 1])
        if pair in all_distances:
            total_distance += all_distances[pair]
        else:
            missing_pairs.append(pair)

    if missing_pairs:
        st.error(f"Distance data missing for pairs: {missing_pairs}. Cannot calculate full route cost.")
    else:
        st.markdown(f"**Total Distance:** {total_distance} km")

        st.markdown("### Transport Options and Estimated Costs:")
        for transport, cost_per_km in transport_options.items():
            cost = total_distance * cost_per_km
            st.write(f"- {transport}: ₹{cost:.2f}")

    st.markdown("### 🖼️ Images of Selected Places:")
    cols = st.columns(len(selected_places))
    for idx, place in enumerate(selected_places):
        cols[idx].image(places[place], caption=place, use_column_width=True)

# Session state to store visited places across interactions
if "visited_places" not in st.session_state:
    st.session_state.visited_places = set()

# Button to mark selected places as visited
if selected_places:
    if st.button("Mark Selected Places as Visited"):
        for place in selected_places:
            st.session_state.visited_places.add(place)
        st.success(f"Added {len(selected_places)} place(s) to visited list.")

# Visited places dashboard
st.markdown("---")
st.subheader("📋 Visited Places Dashboard")

if st.session_state.visited_places:
    visited_list = list(st.session_state.visited_places)
    st.write(f"Total Places Visited: **{len(visited_list)}**")

    # Show images of visited places
    cols = st.columns(len(visited_list))
    for idx, place in enumerate(visited_list):
        cols[idx].image(places[place], caption=place, use_column_width=True)

    # Show a simple bar chart with count of visited places
    st.bar_chart({"Places Visited": [len(visited_list)]})
else:
    st.info("No places visited yet. Select some places and click 'Mark Selected Places as Visited'.")

