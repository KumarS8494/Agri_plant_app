import streamlit as st
from PIL import Image
import torch
from Model_logic_wheat_white_logic import load_model, preprocess_image, class_names, remedies, original_labels, amp_autocast
from io import BytesIO
import base64


def display_image_fixed_size(image, width, height):
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode()

    # Render with fixed width and height
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{img_base64}" width="{width}" height="{height}" style="border-radius: 10px; border: 1px solid #ddd;" />
        </div>
    """, unsafe_allow_html=True)



def render_wheat_white_ear():

    # ====== Stylish Title ======
    st.markdown("""
        <h1 style='text-align: center; font-size: 32px;'>
            🍃 <span style='font-family:Georgia;'><em>WhiteEarScan</em></span>: Wheat White Ear Infestation Analyzer
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
       <p style='text-align: center; font-size: 18px;'>
    An AI-powered tool for detecting <strong>white ear severity in wheat plants</strong> or confirming a <strong>healthy wheat crop</strong>.
</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== Upload Section with Expander ======
    st.markdown("### 📸 Upload a Sample of Image")

    with st.expander("ℹ️ Sample Image Upload Guidelines", expanded=False):
        st.markdown("""
        - Make sure the plant is clearly visible (leaves & stems).
        - Use images in **JPG** or **PNG** format.
        - Keep file size under **200MB** for smooth upload.
        """)

    uploaded_file = st.file_uploader("📤 Drag and drop or browse files", type=["jpg", "jpeg", "png"])

    # ====== Image Preview ======
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        display_image_fixed_size(image, width=800, height=300)
        st.markdown("---")
        # ====== Predict Button ======
        if st.button("🔍 Predict Diagnosis", use_container_width=True):
            model = load_model()
            input_tensor = preprocess_image(image)

            with st.spinner("🔍 Analyzing image..."):
                with amp_autocast():
                    output = model(input_tensor)
                    pred_idx = output.argmax(1).item()

            predicted_class = class_names[pred_idx]
            remedy = remedies[original_labels[pred_idx]]

            # ====== Results ======
            st.success(f"### 🧪 Diagnosis: `{predicted_class}`")
            st.info(f"💡 **Recommendation**: {remedy}")
