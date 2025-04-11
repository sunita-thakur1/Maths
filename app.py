import streamlit as st
from sympy import symbols, Eq, solve, simplify, diff, integrate, sympify
from sympy.parsing.sympy_parser import parse_expr

st.set_page_config(page_title="📚 SymPy Math Solver", layout="centered")
st.title("🧠 SymPy: Step-by-Step Math Solver")

st.markdown("""
Welcome to the **SymPy Math Solver App**! This tool uses the open-source symbolic math library `sympy` to solve math problems step-by-step.

### What You Can Do:
- Solve algebraic equations
- Simplify expressions
- Differentiate functions
- Integrate expressions
""")

# User input
st.header("🔢 Enter Your Math Problem")
problem_type = st.selectbox("What would you like to do?", [
    "Solve Equation",
    "Simplify Expression",
    "Differentiate",
    "Integrate"
])

user_input = st.text_area("Type your expression or equation:", height=100)

x, y = symbols('x y')  # Add more if needed

if st.button("🧮 Compute") and user_input.strip():
    try:
        st.markdown("### ✅ Result")

        if problem_type == "Solve Equation":
            # Expecting input like '2*x + 3 - 7 = 0'
            if '=' in user_input:
                lhs, rhs = user_input.split('=')
                equation = Eq(sympify(lhs), sympify(rhs))
            else:
                equation = Eq(sympify(user_input), 0)
            solution = solve(equation)
            st.code(f"Solution: {solution}")

        elif problem_type == "Simplify Expression":
            expr = sympify(user_input)
            simplified = simplify(expr)
            st.code(f"Simplified: {simplified}")

        elif problem_type == "Differentiate":
            expr = sympify(user_input)
            derivative = diff(expr, x)
            st.code(f"Derivative with respect to x: {derivative}")

        elif problem_type == "Integrate":
            expr = sympify(user_input)
            integral = integrate(expr, x)
            st.code(f"Indefinite Integral with respect to x: {integral} + C")

    except Exception as e:
        st.error(f"❌ Error processing input: {e}")
else:
    st.info("Enter a valid math expression and click 'Compute' to see the result.")

st.markdown("---")
st.markdown("🧑‍🏫 Powered by `SymPy`, a Python library for symbolic mathematics.")
