import streamlit as st



def unit_converter(value: float, unit_from: str, unit_to: str):
    # print("value>>>", value)
    # print("unit_from>>>",unit_from)
    # print("unit_to>>>", unit_to)

    # 1 kilometer = 1000 meter
    # 1 meter = 0.001 kilometer
    # 1 kilogram = 1000 gram
    # 1 gram = 0.001 kilogram

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    if unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    if unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    if unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else: 
        return"conversion is not supported"
    
# result1 = unit_converter(3, "kilometers", "meters")
# print("The value in meter is:", result1)
# result2 = unit_converter(5, "grams", "kilograms")
# print("The value in  kilograms is:", result2)

def main():

    st.title("unit Converter")
    st.write("Welcome to Unit Converter!")

    value= st.number_input("Enter the value you want to convert:",min_value=0.0)
    # unit_from= st.text_input("Enter the value you want convert: (e.g. kilometers, meters, grams, kilograsm)")
    # unit_to= st.text_input("Enter the value you want from conversion: (e.g. kilometers, meters, grams, kilograsm)")
    units = ["kilometers", "meters", "grams", "kilograms"]
    unit_from = st.selectbox("Convert from:", units)
    unit_to = st.selectbox("Convert to:", units)



    if st.button("convert"):
        result= unit_converter(value,unit_from, unit_to)
        st.write("Converted value is:", result)


    # print("unit Converter")
    # print("Welcome to Unit Converter!")
    # value= float (input("Enter the value you want to convert:"))
    # unit_from= input("Enter the value you want convert (e.g. kilometers, meters, grams, kilograsm)")
    # unit_to= input("Enter the value you want from conversion (e.g. kilometers, meters, grams, kilograsm)")

    # print("value", value)
    # print("unit_from", unit_from)
    # print("unit_to", unit_to)
    # result= unit_converter(value,unit_from, unit_to)
    # print("Converted value is:", result)

main()


st.markdown("""
<style>
/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #e0f7fa, #e1bee7);
    background-attachment: fixed;
}

/* Marquee Style */
#custom-marquee {
    position: fixed;
    bottom: 10px;
    right: 10px;
    font-size: 20px;
    color: #6A1B9A;
    font-weight: bold;
    animation: scroll-left 10s linear infinite;
    white-space: nowrap;
}

@keyframes scroll-left {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}
</style>

<div id="custom-marquee">🚀 Made by Malik Wahab</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #e1bee7);
        background-attachment: fixed;
    }

    /* Optional: Make titles look better */
    .stApp h1 {
        color: #4A148C;
        text-shadow: 1px 1px 2px #ccc;
    }

    /* Optional: Adjust the default text color */
    .stApp {
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

