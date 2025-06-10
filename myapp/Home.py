import streamlit as st

def home_page():
    st.title("🛺 Jaipur Multi-Stop Route & Transport Planner")

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

    # Transport options with cost/km
    transport_options = {"Auto-rickshaw": 10, "Taxi": 15, "Bus": 5}

    # Distances between landmarks
    distances = {
        ("Hawa Mahal", "Jal Mahal"): 5, ("Hawa Mahal", "Amber Fort"): 11, ("Hawa Mahal", "City Palace"): 2,
        ("Hawa Mahal", "Jantar Mantar"): 1.5, ("Hawa Mahal", "Birla Mandir"): 7, ("Hawa Mahal", "Albert Hall Museum"): 3,
        ("Hawa Mahal", "Nahargarh Fort"): 9, ("Hawa Mahal", "Galta Ji Temple"): 15, ("Hawa Mahal", "Central Park Jaipur"): 6,

        ("Jal Mahal", "Amber Fort"): 10, ("Jal Mahal", "City Palace"): 5, ("Jal Mahal", "Jantar Mantar"): 4.5,
        ("Jal Mahal", "Birla Mandir"): 6, ("Jal Mahal", "Albert Hall Museum"): 7, ("Jal Mahal", "Nahargarh Fort"): 11,
        ("Jal Mahal", "Galta Ji Temple"): 12, ("Jal Mahal", "Central Park Jaipur"): 9,

        ("Amber Fort", "City Palace"): 13, ("Amber Fort", "Jantar Mantar"): 12, ("Amber Fort", "Birla Mandir"): 18,
        ("Amber Fort", "Albert Hall Museum"): 14, ("Amber Fort", "Nahargarh Fort"): 4, ("Amber Fort", "Galta Ji Temple"): 16,
        ("Amber Fort", "Central Park Jaipur"): 12,

        ("City Palace", "Jantar Mantar"): 1, ("City Palace", "Birla Mandir"): 6, ("City Palace", "Albert Hall Museum"): 2,
        ("City Palace", "Nahargarh Fort"): 8, ("City Palace", "Galta Ji Temple"): 13, ("City Palace", "Central Park Jaipur"): 5,

        ("Jantar Mantar", "Birla Mandir"): 7, ("Jantar Mantar", "Albert Hall Museum"): 2, ("Jantar Mantar", "Nahargarh Fort"): 9,
        ("Jantar Mantar", "Galta Ji Temple"): 13, ("Jantar Mantar", "Central Park Jaipur"): 6,

        ("Birla Mandir", "Albert Hall Museum"): 7, ("Birla Mandir", "Nahargarh Fort"): 14,
        ("Birla Mandir", "Galta Ji Temple"): 17, ("Birla Mandir", "Central Park Jaipur"): 11,

        ("Albert Hall Museum", "Nahargarh Fort"): 9, ("Albert Hall Museum", "Galta Ji Temple"): 14,
        ("Albert Hall Museum", "Central Park Jaipur"): 4,

        ("Nahargarh Fort", "Galta Ji Temple"): 18, ("Nahargarh Fort", "Central Park Jaipur"): 10,
        ("Galta Ji Temple", "Central Park Jaipur"): 20
    }

    # Add reverse directions
    all_distances = distances.copy()
    for (start, end), dist in distances.items():
        all_distances[(end, start)] = dist

    selected = st.multiselect("Select Jaipur places to visit:", list(places.keys()))

    if len(selected) >= 2:
        st.subheader("Route:")
        st.markdown(" → ".join(selected))

        total = 0
        for i in range(len(selected) - 1):
            key = (selected[i], selected[i + 1])
            if key in all_distances:
                total += all_distances[key]

        st.success(f"Total Distance: {total} km")

        st.subheader("Cost Estimate:")
        for mode, cost_km in transport_options.items():
            st.write(f"{mode}: ₹{cost_km * total:.2f}")

        if st.button("Mark as Visited"):
            for place in selected:
                if place not in st.session_state.visited_places:
                    st.session_state.visited_places.append(place)
            st.success("Places marked as visited!")

        st.subheader("📸 Images")
        cols = st.columns(len(selected))
        for i, place in enumerate(selected):
            cols[i].image(places[place], caption=place, use_column_width=True)
    else:
        st.info("Select at least 2 places to view the route.")
