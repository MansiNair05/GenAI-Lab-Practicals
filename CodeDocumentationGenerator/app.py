
import streamlit as st
import ast

st.set_page_config(page_title="AI Code Documentation Generator", page_icon="📝")

st.title("📝 Code Documentation Generator")
st.write("Generate clear documentation for your Python code.")

code = st.text_area(
    "Paste your Python code here:",
    height=250,
    placeholder="def add(a, b):\n    return a + b"
)

if st.button("Generate Documentation"):
    if not code.strip():
        st.warning("Please paste some Python code first.")
    else:
        try:
            tree = ast.parse(code)
            st.subheader("Code Documentation")
            functions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
            classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

            st.markdown("### Program Overview")
            st.write("This program contains Python code that can be analyzed for functions, classes, parameters, and docstrings.")

            st.markdown("### Functions")
            if functions:
                for function in functions:
                    st.markdown(f"**Function:** `{function.name}`")
                    parameters = [arg.arg for arg in function.args.args]
                    st.write("Parameters:", ", ".join(parameters) if parameters else "None")
                    st.write("Existing docstring:", ast.get_docstring(function) or "No docstring found.")
            else:
                st.write("No functions found.")

            st.markdown("### Classes")
            if classes:
                for cls in classes:
                    st.write(f"- {cls.name}")
            else:
                st.write("No classes found.")

            st.success("Documentation analysis completed!")
        except SyntaxError as error:
            st.error(f"Python syntax error: {error}")

st.caption("Note: This demo analyzes Python code locally; it does not call an AI API.")
