import streamlit as st
import graphviz
import json

from backend.mindmap import generate_mindmap

st.set_page_config(
    page_title="AI Mind Map",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Mind Map Generator")

st.write("Generate a visual mind map from your uploaded study material.")


def create_graph(data):

    graph = graphviz.Digraph("MindMap")
    graph.attr(rankdir="TB")

    root = data["root"]

    graph.node(root, root, shape="box", style="filled", fillcolor="lightblue")

    for branch in data["branches"]:

        branch_name = branch["title"]

        graph.node(
            branch_name,
            branch_name,
            shape="ellipse",
            style="filled",
            fillcolor="lightgreen"
        )

        graph.edge(root, branch_name)

        for item in branch["items"]:

            graph.node(
                item,
                item,
                shape="note",
                style="filled",
                fillcolor="lightyellow"
            )

            graph.edge(branch_name, item)

    return graph


if st.button("🧠 Generate Mind Map"):

    with st.spinner("Generating Mind Map..."):

        mindmap_text = generate_mindmap()

    try:

        mindmap = json.loads(mindmap_text)

        st.success("✅ Mind Map Generated Successfully!")

        graph = create_graph(mindmap)

        st.graphviz_chart(graph)

        with st.expander("📄 JSON Output"):

            st.json(mindmap)

        st.download_button(
            label="📥 Download Mind Map",
            data=json.dumps(mindmap, indent=4),
            file_name="EcoEdith_MindMap.json",
            mime="application/json"
        )

    except Exception as e:

        st.error("❌ Failed to generate a valid mind map.")

        st.code(mindmap_text)

        st.exception(e)