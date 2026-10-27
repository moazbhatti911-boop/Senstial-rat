import os
import importlib

import httpx

try:
    st = importlib.import_module("streamlit")
except ModuleNotFoundError as exc:
    if exc.name != "streamlit":
        raise
    raise SystemExit(
        "Streamlit is required. Install it with: python -m pip install streamlit"
    ) from exc

st.set_page_config(
    page_title="SentinelRAT Dashboard",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ SentinelRAT")
st.caption("Authorized Endpoint Monitoring Dashboard")

api_url = st.sidebar.text_input(
    "API URL",
    value="http://127.0.0.1:8000",
)

api_key = st.sidebar.text_input(
    "API Key",
    value=os.getenv("SENTINEL_API_KEY", ""),
    type="password",
)

if st.sidebar.button("Refresh dashboard"):
    st.rerun()

if not api_key:
    st.info("Enter your API key in the sidebar.")
    st.stop()

headers = {"X-API-Key": api_key}

try:
    with httpx.Client(
        base_url=api_url.rstrip("/"),
        headers=headers,
        timeout=5.0,
    ) as client:
        health_response = client.get("/health")
        health_response.raise_for_status()

        devices_response = client.get("/devices/")
        devices_response.raise_for_status()

        devices = devices_response.json()

    st.success("API connection established.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Enrolled devices", len(devices))

    with col2:
        st.metric("API status", "Online")

    st.subheader("Registered Devices")

    if devices:
        st.dataframe(
            devices,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info(
            "No devices enrolled yet. "
            "Register a test device using the API."
        )

except httpx.HTTPStatusError as exc:
    if exc.response.status_code == 401:
        st.error("Authentication failed. Check your API key.")
    else:
        st.error(
            f"API returned HTTP {exc.response.status_code}."
        )

except httpx.HTTPError as exc:
    st.error(f"Could not connect to the API: {exc}")